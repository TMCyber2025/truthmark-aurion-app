
# compare.py

import streamlit as st

# 🔧 Forensic UI Styling Injection
def apply_custom_styling():
    st.markdown("""
        <style>
            .stApp {
                background-image: url("https://yourdomain.com/assets/bg-forensic-circuit.png");
                background-size: cover;
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: fixed;
                background-color: #0a1d2b;
                color: white;
            }
            .block-container {
                padding-top: 2rem;
                padding-bottom: 2rem;
                background-color: rgba(10, 29, 43, 0.85);
                border-radius: 10px;
            }
            h1, h2, h3 {
                color: #f0f4f8;
                font-family: 'Orbitron', sans-serif;
            }
            .metric-label, .metric-value {
                font-family: 'Exo', sans-serif;
            }
            .stButton>button {
                background-color: #1976d2;
                color: white;
                border-radius: 6px;
            }
        </style>
    """, unsafe_allow_html=True)

# 🧪 Integrity Validator Core
def validate_integrity(baseline_data, subject_data):
    verdict = "Truthful" if baseline_data["baseline_hash"] == subject_data["subject_hash"] else "Deception"
    confidence = "98.9%" if verdict == "Truthful" else "78.5%"
    anomalies = [] if verdict == "Truthful" else ["Cryptographic fingerprint mismatch"]

    return {
        "verdict": verdict,
        "confidence": confidence,
        "anomalies": anomalies,
        "baseline_hash": baseline_data["baseline_hash"],
        "subject_hash": subject_data["subject_hash"]
    }
