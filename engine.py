import cv2
import numpy as np
import librosa
import tempfile
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
    return filtered[:300], heart_rate, hrv_std

def compute_ear(frames):
    ear_trace = []
    for frame in frames[:300]:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ear_val = np.var(gray) / 255
        ear_trace.append(ear_val)
    blink_rate = sum(1 for e in ear_trace if e < 0.15) / len(ear_trace)
    return ear_trace, blink_rate

def extract_mfcc(path):
    y, sr = librosa.load(path, sr=None)
    y_resampled = librosa.resample(y, orig_sr=sr, target_sr=16000)
    mfcc = librosa.feature.mfcc(y=y_resampled, sr=16000)
    return mfcc.mean(axis=1)

def cosine_distance(v1, v2):
    if len(v1) != len(v2): return 1.0
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    if norm_v1 == 0 or norm_v2 == 0: return 1.0
    return round(1.0 - np.dot(v1, v2) / (norm_v1 * norm_v2), 3)

def analyze_with_baseline(baseline_file, subject_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as f1:
        f1.write(baseline_file.getbuffer())
        baseline_path = f1.name
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as f2:
        f2.write(subject_file.getbuffer())
        subject_path = f2.name

    # Extract frames
    base_frames = extract_frames(baseline_path)
    subj_frames = extract_frames(subject_path)

    # Compute biometric features
    base_rppg, base_hr, base_hrv = compute_rppg(base_frames)
    subj_rppg, subj_hr, subj_hrv = compute_rppg(subj_frames)

    base_ear, base_blink = compute_ear(base_frames)
    subj_ear, subj_blink = compute_ear(subj_frames)

    # MFCC semantic comparison
    base_mfcc = extract_mfcc(baseline_path)
    subj_mfcc = extract_mfcc(subject_path)
    drift_score = cosine_distance(base_mfcc, subj_mfcc)

    # Deltas
    hrv_delta = round(subj_hrv - base_hrv, 3)
    blink_delta = round(subj_blink - base_blink, 3)

    verdict = "Truthful ✅"
    if hrv_delta > 0.15 or drift_score > 0.3 or abs(blink_delta) > 0.1:
        verdict = "Inconsistent ⚠️"

    return {
        "base_hr": round(base_hr, 1),
        "subj_hr": round(subj_hr, 1),
        "hrv_delta": hrv_delta,
        "blink_delta": blink_delta,
        "drift_score": drift_score,
        "verdict": verdict,
        "rppg_curves": {"baseline": base_rppg, "subject": subj_rppg},
        "ear_curves": {"baseline": base_ear, "subject": subj_ear},
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
