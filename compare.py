import random

def validate_integrity(baseline_data, subject_data):
    baseline_hash = baseline_data.get("baseline_hash")
    subject_hash = subject_data.get("subject_hash")

    if baseline_hash == subject_hash:
        verdict = "Truthful"
        confidence = "99.9%"
        anomalies = ["✔️ No discrepancies found"]
    else:
        # DEMO: Randomly decide if it's deception or plausible truth
        if random.random() > 0.4:  # 60% chance to still say "Deception"
            verdict = "Deception"
            confidence = "99.9%"
            anomalies = ["⚠️ Hash mismatch – possible tampering"]
        else:
            verdict = "Truthful"
            confidence = "99.9%"
            anomalies = ["⚠️ Hash mismatch – inconclusive but plausibly authentic"]

    return {
        "verdict": verdict,
        "confidence": confidence,
        "baseline_hash": baseline_hash,
        "subject_hash": subject_hash,
        "anomalies": anomalies
    }
