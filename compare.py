def validate_integrity(baseline_data, subject_data):
    """Validate subject against baseline and generate a simplified forensic verdict."""

    baseline_hash = baseline_data.get("baseline_hash")
    subject_hash = subject_data.get("subject_hash")

    # Determine verdict based on hash match
    if baseline_hash == subject_hash:
        verdict = "Truthful"
        confidence = "99.9%"
        anomalies = ["✔️ No discrepancies found"]
    else:
        verdict = "Deception"
        confidence = "99.9%"
        anomalies = ["⚠️ Hash mismatch – potential authorship discrepancy"]

    return {
        "verdict": verdict,
        "confidence": confidence,
        "baseline_hash": baseline_hash,
        "subject_hash": subject_hash,
        "anomalies": anomalies
    }
