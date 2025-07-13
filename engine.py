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
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

def compute_rppg(frames):
    g_signal = [frame[:, :, 1].mean() for frame in frames]  # green channel signal
    b, a = butter(2, [0.7/30, 2.5/30], btype='band')
    filtered = filtfilt(b, a, g_signal)
    peaks, _ = find_peaks(filtered, distance=30)
    heart_rate = len(peaks) * 2  # approx. BPM over ~15 seconds
    rr_intervals = np.diff(peaks)
    hrv_std = float(np.std(rr_intervals)) if len(rr_intervals) > 1 else 0.0
    return filtered, heart_rate, hrv_std

def compute_ear(frames):
    ear_trace = []
    for frame in frames[:300]:  # first 300 frames only
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ear_val = np.var(gray) / 255  # simplified attention proxy
        ear_trace.append(ear_val)
    blink_rate = sum(1 for e in ear_trace if e < 0.15) / len(ear_trace)
    return ear_trace, blink_rate

def compute_semantic_drift(audio_path, transcript):
    try:
        y, sr = librosa.load(audio_path, sr=None)
        y_resampled = librosa.resample(y, orig_sr=sr, target_sr=16000)
        mfcc = librosa.feature.mfcc(y=y_resampled, sr=16000)
    except Exception as e:
        print("Semantic drift audio error:", e)
        return 0.0

    baseline = "This is the expected baseline context."
    overlap = len(set(transcript.split()) & set(baseline.split()))
    drift_score = round(1.0 - overlap / max(len(transcript.split()), 1), 3)
    return drift_score

def analyze_evidence(uploaded_file, transcript=None, external_audio=None):
    # Save uploaded video file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(uploaded_file.getbuffer())
        video_path = temp_video.name

    frames = extract_frames(video_path)
    rppg_curve, heart_rate, hrv_std = compute_rppg(frames)
    ear_curve, blink_rate = compute_ear(frames)

    # Fallback transcript if none provided
    if not transcript:
        transcript = "This is the user's uploaded transcript."

    # Use external audio file or fall back to embedded (assumes audio is embedded in video)
    audio_path = external_audio or video_path
    drift_score = compute_semantic_drift(audio_path, transcript)

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
