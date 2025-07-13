# compare.py

import streamlit as st

# 🔧 Forensic Styling: Visual Elevation
def apply_custom_styling():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Exo&display=swap');

            .stApp {
                background-image: linear-gradient(135deg, #0e2237 0%, #144361 100%), url("https://yourdomain.com/assets/bg-forensic-circuit.png");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
                color: #e2ecf2;
                font-family: 'Exo', sans-serif;
            }

            .block-container {
                padding: 3rem 2rem;
                background-color: rgba(13, 30, 48, 0.85);
                border-radius: 14px;
                box-shadow: 0 0 12px rgba(0, 0, 0, 0.25);
            }

            h1, h2, h3 {
                color: #f8fafe;
                font-family: 'Orbitron', sans-serif;
                letter-spacing: 0.9px;
                text-transform: uppercase;
            }

            .markdown-text-container, label, p {
                color: #cdd7e2;
                font-size: 0.95rem;
                line-height: 1.6;
            }

            .stButton>button {
                background-color: #1976d2;
                border-radius: 6px;
                padding: 0.6rem 1.2rem;
                font-weight: 600;
                color: #fff;
                transition: 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #145ea1;
            }

            .stMetric {
                background-color: rgba(255, 255, 255, 0.05);
                border-radius: 10px;
                padding: 0.5rem;
                margin-bottom: 0.5rem;
            }

            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

# 🧪 Biometric Integrity Validator
def validate_integrity(baseline_data, subject_data):
    baseline_hash = baseline_data["baseline_hash"]
    subject_hash = subject_data["subject_hash"]

    # 🔐 Cryptographic Match
    cryptographic_match = baseline_hash == subject_hash

    # 🧠 Facial Geometry (placeholder)
    facial_similarity_score = 0.94
    facial_geometry_ok = facial_similarity_score >= 0.90

    # 🎙️ Voiceprint Consistency (placeholder)
    voice_consistency = True

    # ⏱️ Timestamp Drift Analysis (placeholder)
    timestamp_drift_seconds = 0.7
    drift_acceptable = timestamp_drift_seconds < 1.0

    # 🧮 Verdict Calculation
    if all([cryptographic_match, facial_geometry_ok, voice_consistency, drift_acceptable]):
        verdict = "Truthful"
        confidence = "98.9%"
        anomalies = []
    else:
        verdict = "Deception"
        confidence = "78.5%"
        anomalies = []
        if not cryptographic_match:
            anomalies.append("❌ Cryptographic hash mismatch")
        if not facial_geometry_ok:
            anomalies.append(f"⚠️ Facial geometry score too low ({facial_similarity_score})")
        if not voice_consistency:
            anomalies.append("🔊 Voiceprint inconsistency detected")
        if not drift_acceptable:
            anomalies.append(f"⏱️ Timestamp drift exceeds threshold: {timestamp_drift_seconds}s")

    return {
        "verdict": verdict,
        "confidence": confidence,
        "anomalies": anomalies,
        "baseline_hash": baseline_hash,
        "subject_hash": subject_hash
    }
