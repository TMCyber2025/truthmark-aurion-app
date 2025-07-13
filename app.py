# app.py

import streamlit as st
from engine import run_demo
from upload_webcam import capture_webcam
import os

# 🚀 Page Config
st.set_page_config(page_title="TruthMark-Aurion: Guardian of the Truth", layout="centered")

# 🎨 Forensic Styling
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Exo&display=swap" rel="stylesheet">
<style>
    .stApp {
        background-image: url("https://yourdomain.com/assets/bg-forensic-circuit-lightblue.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
        background-color: #0e2a45;
    }
    .block-container {
        padding-top: 4rem;
        padding-bottom: 4rem;
        background-color: rgba(14, 42, 69, 0.85);
        border-radius: 12px;
    }
    h1, h2, h3 {
        color: #f0f4f8;
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 0.8px;
    }
    p, label, .markdown-text-container {
        color: #cfd8e3;
        font-family: 'Exo', sans-serif;
    }
    .stButton>button {
        background-color: #1976d2;
        color: white;
        font-weight: 600;
        border-radius: 6px;
        padding: 0.6rem 1.2rem;
    }
    .stMetric {
        background-color: rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        padding: 0.5rem;
    }
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 🛡️ Title Zone
st.title("🛡️ TruthMark-Aurion")
st.subheader("Guardian of the Truth — Validate. Detect. Preserve.")

# 📘 Instructions
st.markdown("""
Welcome to the live demo of TruthMark-Aurion’s forensic validation engine.  
Upload your verified **Baseline Video** and a **Subject Video** (or record via webcam), then click _Run Forensic Validation_ to receive a verdict in seconds.
""")

# 📁 Sidebar Uploads
st.sidebar.header("📁 Upload Inputs")

baseline_video = st.sidebar.file_uploader("🎞️ Baseline Video", type=["mp4", "mov"])
subject_video = st.sidebar.file_uploader("📽️ Subject Video", type=["mp4", "mov"])

use_webcam = st.sidebar.checkbox("📷 Use Webcam for Subject Input")
if use_webcam and st.sidebar.button("Start Webcam Capture"):
    capture_webcam("uploads/webcam_input.mp4")
    st.sidebar.success("Webcam video saved to uploads/webcam_input.mp4")

# 💾 Save File Utility
def save_file(uploaded, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(uploaded.getbuffer())
    return path

# 🧠 Verdict Processor
if st.button("Run Forensic Validation"):
    st.markdown("### 📽️ Processing Videos... Please wait.")
    with st.spinner("Analyzing input data..."):

        # ✅ Baseline Check
        if baseline_video is not None:
            base_path = save_file(baseline_video, "data/baseline.mp4")
        else:
            st.error("❌ Please upload a Baseline Video.")
            st.stop()

        # ✅ Subject Check
        if use_webcam and os.path.exists("uploads/webcam_input.mp4"):
            subject_path = "uploads/webcam_input.mp4"
            st.info("Using webcam input as subject video.")
        elif subject_video is not None:
            subject_path = save_file(subject_video, "data/subject.mp4")
        else:
            st.error("❌ Please upload a Subject Video or use Webcam.")
            st.stop()

        # 🔍 Forensic Validation
        try:
            result = run_demo(base_path, subject_path, "", "")
        except Exception as e:
            st.error(f"⚠️ Validation error: {e}")
            st.stop()

        if not isinstance(result, dict):
            st.error("⚠️ No valid validation result returned. Please check input files.")
            st.stop()

        # 🎯 Display Result
        verdict = result.get("verdict", "Undetermined")
        confidence = result.get("confidence", "N/A")
        anomalies = result.get("anomalies", [])
        baseline_hash = result.get("baseline_hash", "")
        subject_hash = result.get("subject_hash", "")

        st.subheader("🧠 Validation Outcome")
        st.markdown(f"### Verdict: **{verdict}**")
        st.metric(label="Confidence Score", value=confidence)

        if verdict.lower() == "truthful":
            st.success("✅ Evidence aligns with baseline. No discrepancies detected.")
        elif verdict.lower() == "deception":
            st.error("🚨 Integrity breach detected. Evidence does not match baseline.")
        else:
            st.warning("⚠️ Verdict unclear. Further analysis recommended.")

        st.markdown("#### 🔐 Evidence Fingerprints")
        st.code(f"Baseline Hash: {baseline_hash}\nSubject Hash: {subject_hash}", language="text")

        st.markdown("#### 🔍 Anomaly Flags")
        if anomalies:
            for item in anomalies:
                st.write(f"- {item}")
        else:
            st.write("No anomalies detected.")

        try:
            percent = float(confidence.strip("%")) / 100
            st.progress(percent)
        except:
            pass

        with st.expander("🎬 Preview Videos"):
            st.video(base_path)
            st.video(subject_path)
