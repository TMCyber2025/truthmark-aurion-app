# compare.py
import hashlib
import difflib

def generate_hash(file_path):
    """Generate a SHA-256 hash for the given file."""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def compare_hashes(baseline_hash, subject_hash):
    """Compare hash strings and return similarity score."""
    return 1.0 if baseline_hash == subject_hash else 0.0

def compare_notes(baseline_notes, subject_notes):
    """Score textual similarity using sequence matching."""
    matcher = difflib.SequenceMatcher(None, baseline_notes, subject_notes)
    return matcher.ratio()

def validate_integrity(baseline_data, subject_data):
    """Validate subject against baseline and generate a forensic report."""
    baseline_hash = baseline_data.get("baseline_hash")
    subject_hash = subject_data.get("subject_hash")

    notes_score = compare_notes(baseline_data.get("notes", ""), subject_data.get("notes", ""))
    hash_score = compare_hashes(baseline_hash, subject_hash)

    anomalies = []
    if hash_score < 1.0:
        anomalies.append("⚠️ Hash mismatch – potential authorship discrepancy")
    if notes_score < 0.8:
        anomalies.append("⚠️ Metadata notes differ significantly")

    integrity_index = round((hash_score + notes_score) / 2, 3)

    return {
        "baseline_hash": baseline_hash,
        "subject_hash": subject_hash,
        "match_confidence": integrity_index,
        "anomalies": anomalies or ["✔️ No anomalies detected"]
    }
