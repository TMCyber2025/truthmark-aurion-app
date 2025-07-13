# engine.py
import hashlib
from compare import validate_integrity

def generate_hash(file_path):
    """Generate a SHA-256 hash for the given file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def process_baseline(baseline_video, baseline_txt=None):
    """Process baseline input: video + optional metadata."""
    baseline_hash = generate_hash(baseline_video)

    notes = ""
    if baseline_txt:
        try:
            with open(baseline_txt, "r") as f:
                notes = f.read()
        except Exception:
            notes = "No metadata available."

    return {"baseline_hash": baseline_hash, "notes": notes}

def process_subject(subject_video, subject_txt=None):
    """Process subject input: video + optional metadata."""
    subject_hash = generate_hash(subject_video)

    notes = ""
    if subject_txt:
        try:
            with open(subject_txt, "r") as f:
                notes = f.read()
        except Exception:
            notes = "No metadata available."

    return {"subject_hash": subject_hash, "notes": notes}

def compare_inputs(baseline_data, subject_data):
    """Pass processed inputs to integrity validator."""
    return validate_integrity(baseline_data, subject_data)

def run_demo(baseline_video, subject_video, baseline_txt=None, subject_txt=None):
    """Primary demo runner: orchestrates entire process."""
    base = process_baseline(baseline_video, baseline_txt)
    subj = process_subject(subject_video, subject_txt)
    result = compare_inputs(base, subj)
    return result
