# app.py
import streamlit as st
from engine import run_demo
from upload_webcam import capture_webcam
import os

# Page Setup
st.set_page_config(page_title="TruthMark-Aurion Demo", layout="centered")
st.title("🔍 TruthMark-Aurion: Forensic Integrity Demo")

# 📘 Instructions
st.markdown("""
### 👣 How to Use:
1. Upload a **Baseline Video** – your verified source material.  
2. Upload a **Subject Video** – the evidence you want to compare.  
3. Alternatively, use the webcam to simulate live input.  
Click **Run Forensic Validation** to assess integrity and detect anomalies.
""")

# 📁 Sidebar Inputs
st.sidebar.header("📁 Upload Inputs")

baseline_video = st.sidebar.file_uploader("🎞️ Baseline Video", type=["mp4", "mov"], key="baseline")
subject_video = st.sidebar.file_uploader("📽️ Subject Video", type=["mp4", "mov"], key="subject")

use_webcam = st.sidebar.checkbox("📷 Use Webcam for Subject Input")
if use_webcam and st.sidebar.button("Start Webcam Capture"):
    capture_webcam("uploads/webcam_input.mp4")
    st.sidebar.success("Webcam video saved to uploads/webcam_input.mp4")

# 💾 File Saver
def save_file(uploaded, path):
    with open(path, "wb") as f:
        f.write(uploaded.getbuffer())
    return path

# 🚀 Run Validation
if st.button("Run Forensic Validation"):
    with st.spinner("Running integrity analysis..."):

        # Use webcam + baseline
        if use_webcam and baseline_video and os.path.exists("uploads/webcam_input.mp4"):
            base_path = save_file(baseline_video, "data/baseline.mp4")
            webcam_path = "uploads/webcam_input.mp4"

            result = run_demo(base_path, webcam_path, "", "")
            st.subheader("🧠 Webcam-Based Validation Result")
            st.json(result)

        # Use uploaded videos
        elif baseline_video and subject_video:
            base_path = save_file(baseline_video, "data/baseline.mp4")
            subj_path = save_file(subject_video, "data/subject.mp4")

            result = run_demo(base_path, subj_path, "", "")
            st.subheader("🧠 File-Based Validation Result")
            st.json(result)

        else:
            st.error("Please upload both a baseline and subject video, or use webcam + baseline.")
