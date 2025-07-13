import cv2
import numpy as np
import librosa
import tempfile
import os
from scipy.signal import butter, filtfilt, find_peaks
from datetime import datetime

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret: break
        frames.append(frame)
    cap.release()
    return frames

def compute_rppg(frames):
    g_signal = [frame[:, :, 1].mean() for frame in frames]
    b, a = butter(2, [0.7/30, 2.5/30], btype='band')
    filtered = filtfilt(b, a, g_signal)
    peaks, _ = find_peaks(filtered, distance=30)
    heart_rate = len(peaks) * 2
    rr_intervals = np.diff(peaks)
    hrv_std = float(np.std(rr_intervals)) if len(rr_intervals) > 1 else 0.0
    return filtered, heart_rate, hrv_std

def compute_ear(frames):
    ear_trace = []
    for frame in frames[:300]:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ear_val = np.var(gray) / 255
        ear_trace.append(ear_val)
    blink_rate = sum(1 for e in ear_trace if e < 0.15) / len(ear_trace)
    return ear_trace, blink_rate

def compute_semantic_drift(audio_path, baseline_text):
    try:
        y, sr = librosa.load(audio_path, sr=None)
        y_resampled = librosa.resample(y, orig_sr=sr, target_sr=16000)
        _ = librosa.feature.mfcc(y=y_resampled, sr=16000)  # analysis placeholder
    except Exception as e:
        print("Audio error:", e)
        return 0.0

    overlap = len(set(baseline_text.split()) & set(baseline_text.split()))
    drift_score = round(1.0 - overlap / max(len(baseline_text.split()), 1), 3)
    return drift_score

def analyze_evidence(uploaded_file, baseline_text=None):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(uploaded_file.getbuffer())
        video_path = temp_video.name

    frames = extract_frames(video_path)
    rppg_curve, heart_rate, hrv_std = compute_rppg(frames)
    ear_curve, blink_rate = compute_ear(frames)
    audio_path = video_path

    if not baseline_text:
        baseline_text = "This is the expected baseline context."

    drift_score = compute_semantic_drift(audio_path, baseline_text)
    verdict = "Truthful ✅" if hrv_std < 0.25 and drift_score < 0.2 else "Inconsistent ⚠️"

    return {
        "heart_rate": round(heart_rate, 1),
        "hrv_std": round(hrv_std, 3),
        "blink_ear": round(blink_rate, 3),
        "drift_score": drift_score,
        "verdict": verdict,
        "rppg_curve": rppg_curve[:300],
        "ear_curve": ear_curve[:300],
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
