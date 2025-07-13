# app.py
import streamlit as st
from engine import run_demo
from upload_webcam import capture_webcam
import os

st.set_page_config(page_title="TruthMark-Aurion Demo", layout="centered")
st.title("🔍 TruthMark-Aurion: Forensic Integrity Demo")
st.markdown("Upload baseline and subject files or capture webcam input to validate evidence consistency.")

# Sidebar Inputs
st.sidebar.header("📁 Upload Inputs")

baseline_video = st.sidebar.file_uploader("Baseline Video", type=["mp4", "mov"], key="baseline_video")
baseline_txt = st.sidebar.file_uploader("Baseline Metadata (.txt)", type=["txt"], key="baseline_txt")
subject_video = st.sidebar.file_uploader("Subject Video", type=["mp4", "mov"], key="subject_video")
subject_txt = st.sidebar.file_uploader("Subject Metadata (.txt)", type=["txt"], key="subject_txt")

use_webcam = st.sidebar.checkbox("Use Webcam Input")

# Webcam Capture Option
if use_webcam and st.sidebar.button("🎥 Capture Webcam"):
    capture_webcam("uploads/webcam_input.mp4")
    st.sidebar.success("Webcam input saved to uploads/webcam_input.mp4")
    subject_video = "uploads/webcam_input.mp4"

# Run Demo
if st.button("🔎 Run Forensic Validation"):
    with st.spinner("Processing inputs and running integrity checks..."):

        # Save uploaded files locally
        def save_file(uploaded_file, save_path):
            with open(save_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            return save_path

        if baseline_video and baseline_txt and subject_video and subject_txt:
            base_vid_path = save_file(baseline_video, "baseline/video_baseline.mp4")
            base_txt_path = save_file(baseline_txt, "baseline/baseline_meta.txt")
            subj_vid_path = save_file(subject_video, "subject/video_subject.mp4")
            subj_txt_path = save_file(subject_txt, "subject/subject_notes.txt")

            result = run_demo(
                base_vid_path,
                subj_vid_path,
                base_txt_path,
                subj_txt_path
            )

            st.subheader("🧠 Validation Result")
            st.json(result)
        else:
            st.error("Please upload all required files before running the demo.")

# Footer
st.markdown("---")
st.caption("TruthMark-Aurion © 2025 | Preserving evidentiary integrity through biometric and cryptographic verification.")
