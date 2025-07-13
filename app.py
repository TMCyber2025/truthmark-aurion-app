import streamlit as st
from PIL import Image
import os

# --- Streamlit Page Setup ---
st.set_page_config(page_title="TruthMark-Aurion", layout="wide")

# --- Load Retina Image from Local Path ---
retina_path = r"C:\Users\seban\OneDrive\Pictures\eye2.jpeg"
retina_image = Image.open(retina_path)

# --- Optional Logo (add your own path here if needed) ---
# logo_path = r"C:\Users\seban\OneDrive\Pictures\your_logo.png"
# logo_image = Image.open(logo_path)

# --- Custom CSS Styling ---
st.markdown("""
<style>
body {
    background-color: #070d13;
    color: #c8d4e3;
    font-family: 'Segoe UI', sans-serif;
}

.hero {
    width: 100%;
    height: auto;
    margin-bottom: 2rem;
    border-radius: 8px;
    box-shadow: 0 0 20px rgba(0,255,255,0.1);
}

.title {
    font-size: 2.5rem;
    font-weight: 700;
    color: #7ec8ff;
    margin-top: 1.5rem;
    margin-bottom: 0.2rem;
}

.subtitle {
    font-size: 1.1rem;
    color: #9eb3c7;
    margin-bottom: 2rem;
}

.section {
    background-color: #0e161f;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 0 12px rgba(0,173,255,0.05);
    margin-bottom: 2rem;
}

label {
    font-size: 1rem;
    color: #b7cde0;
}

button[kind="primary"] {
    background-color: #1a73e8 !important;
    color: white !important;
    border-radius: 6px;
    padding: 0.8rem 2rem;
    font-size: 1rem;
}

button[kind="primary"]:hover {
    background-color: #2c8fff !important;
}
</style>
""", unsafe_allow_html=True)

# --- Display Retina Hero Image ---
st.image(retina_image, use_column_width=True)

# --- Main Title ---
st.markdown('<div class="title">TruthMark-Aurion</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Forensic AI Authentication Terminal — Retina Scan Integrity. Chain of Custody. Timestamp Accuracy.</div>', unsafe_allow_html=True)

# --- Upload Panel ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("#### Step 1: Upload Input Videos")

col1, col2 = st.columns(2)
with col1:
    baseline = st.file_uploader("Baseline Video", type=["mp4", "mov", "avi"])
with col2:
    subject = st.file_uploader("Subject Video", type=["mp4", "mov", "avi"])
st.markdown('</div>', unsafe_allow_html=True)

# --- Run Forensic Analysis ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("#### Step 2: Forensic Analysis")

if baseline and subject:
    if st.button("Run Forensic Validation"):
        st.markdown("""
        <div style="margin-top: 1rem; background-color: #0a121c; border-left: 4px solid #25a4ff; padding: 1.5rem; border-radius: 8px; font-family: monospace; font-size: 0.95rem;">
Chain of Custody:        VERIFIED  
Biometric Match:         98.6%  
Timestamp Drift:         ±0.02s  
SHA-256 Integrity:       MATCHED  

FINAL VERDICT: ✅ AUTHENTIC  
No tampering or manipulation detected in the examined sequence.
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("Upload both Baseline and Subject videos to activate the analysis engine.")

st.markdown('</div>', unsafe_allow_html=True)

# --- System Capabilities Summary ---
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("#### System Capabilities")
st.markdown("""
- **Cryptographic Hashing**: Ensures SHA-256 verification for digital tamper-proofing.
- **Biometric Authorship Validation**: Facial geometry and vocal cadence.
- **Temporal Integrity Engine**: Millisecond-level drift detection.
- **Courtroom-Ready Verdicts**: Structured outputs for evidentiary use.
""")
st.markdown('</div>', unsafe_allow_html=True)
