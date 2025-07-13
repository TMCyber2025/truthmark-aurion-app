# engine.py
import cv2
import json
from compare import validate_integrity

def process_baseline(baseline_video, baseline_txt):
    # Load video frames and metadata
    # Placeholder: Add biometric hash extraction, timestamp parsing
    return {"baseline_hash": "abc123", "notes": open(baseline_txt).read()}

def process_subject(subject_video, subject_txt):
    return {"subject_hash": "xyz789", "notes": open(subject_txt).read()}

def compare_inputs(baseline_data, subject_data):
    return validate_integrity(baseline_data, subject_data)

def run_demo(baseline_video, subject_video, baseline_txt, subject_txt):
    base = process_baseline(baseline_video, baseline_txt)
    subj = process_subject(subject_video, subject_txt)
    result = compare_inputs(base, subj)
    return result
