# engine.py
import hashlib
from compare import validate_integrity

def generate_hash(file_path):
    """Generate SHA-256 hash from a video file."""
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def process_baseline(baseline_video, baseline_txt=None):
    """Process baseline input and return structured data."""
    baseline_hash = generate_hash(baseline_video)
    return {
        "baseline_hash": baseline_hash,
        "notes": ""  # Metadata not used in demo
    }

def process_subject(subject_video, subject_txt=None):
    """Process subject input and return structured data."""
    subject_hash = generate_hash(subject_video)
    return {
        "subject_hash": subject_hash,
        "notes": ""  # Metadata not used in demo
    }

def compare_inputs(baseline_data, subject_data):
    """Send processed input to integrity validator."""
    return validate_integrity(baseline_data, subject_data)

def run_demo(baseline_video, subject_video, baseline_txt=None, subject_txt=None):
    """Main orchestration for demo — returns result dictionary."""
    baseline_data = process_baseline(baseline_video, baseline_txt)
    subject_data = process_subject(subject_video, subject_txt)
    result = compare_inputs(baseline_data, subject_data)
    return result
