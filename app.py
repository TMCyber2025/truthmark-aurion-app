# app.py
# 🛡️ Hero Banner with Cinematic Styling
st.markdown("""
<div style="text-align: center; padding-top: 2rem; padding-bottom: 1.5rem;">
    <h1 style="font-family: 'Orbitron', sans-serif; font-size: 3.2rem; color: #a3e4ff; margin-bottom: 0;">
        🛡️ TruthMark-Aurion
    </h1>
    <h3 style="font-family: 'Exo', sans-serif; color: #f8fafe; font-weight: 400; margin-top: 0.5rem;">
        Guardian of the Truth — Validate. Detect. Preserve.
    </h3>
</div>
""", unsafe_allow_html=True)

# 📘 Animated Instruction Panel
st.markdown("""
<div style="text-align: center; padding: 1.5rem 2rem; background-color: rgba(14,42,69,0.7); border-radius: 12px; box-shadow: 0 0 12px rgba(0, 0, 0, 0.3);">
    <p style="font-family: 'Exo', sans-serif; font-size: 1.05rem; color: #cfd8e3; line-height: 1.7;">
        Welcome to the live demo of <strong>TruthMark-Aurion</strong>’s forensic validation engine.<br><br>
        Upload your verified <span style="color:#7ec8ff; font-weight:bold;">Baseline Video</span> and <span style="color:#7ec8ff; font-weight:bold;">Subject Video</span> (or record via webcam),<br>then click <em style="color:#a3e4ff;">Run Forensic Validation</em> to receive a courtroom-grade verdict in seconds.
    </p>
</div>
""", unsafe_allow_html=True)

# ✨ Feature Highlights Section
st.markdown("""
<div style="display: flex; justify-content: center; gap: 2rem; margin-top: 2rem; flex-wrap: wrap;">
  <div style="background: rgba(28, 52, 74, 0.85); border-radius: 14px; padding: 1rem 1.5rem; width: 300px; text-align: center; box-shadow: 0 0 10px rgba(0,0,0,0.3);">
    <h4 style="color: #7ec8ff;">🔐 Cryptographic Validation</h4>
    <p style="color: #cfd8e3; font-size: 0.95rem;">Real-time SHA-256 fingerprinting ensures evidentiary integrity from the ground up.</p>
  </div>
  <div style="background: rgba(28, 52, 74, 0.85); border-radius: 14px; padding: 1rem 1.5rem; width: 300px; text-align: center; box-shadow: 0 0 10px rgba(0,0,0,0.3);">
    <h4 style="color: #7ec8ff;">🧬 Biometric Intelligence</h4>
    <p style="color: #cfd8e3; font-size: 0.95rem;">Facial geometry, voiceprint consistency, and timestamp coherence — all analyzed in seconds.</p>
  </div>
  <div style="background: rgba(28, 52, 74, 0.85); border-radius: 14px; padding: 1rem 1.5rem; width: 300px; text-align: center; box-shadow: 0 0 10px rgba(0,0,0,0.3);">
    <h4 style="color: #7ec8ff;">🧠 Verdict Engine</h4>
    <p style="color: #cfd8e3; font-size: 0.95rem;">Clear and concise verdict delivery backed by forensic-grade analytics.</p>
  </div>
</div>
""", unsafe_allow_html=True)
import streamlit as st
from engine import run_demo
from upload_webcam import capture_webcam
from output import (
    display_verdict,
    display_hashes,
    display_anomalies,
    display_progress,
    preview_videos,
)
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

        # 🎯 Display Result (modular via output.py)
        display_verdict(result.get("verdict", "Undetermined"), result.get("confidence", "N/A"))
        display_hashes(result.get("baseline_hash", ""), result.get("subject_hash", ""))
        display_anomalies(result.get("anomalies", []))
        display_progress(result.get("confidence", "0%"))
        preview_videos(base_path, subject_path)
