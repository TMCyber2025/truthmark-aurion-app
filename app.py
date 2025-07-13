# app.py
import streamlit as st
from engine import run_demo
from upload_webcam import capture_webcam
import os

# Page config and layout
st.set_page_config(page_title="TruthMark-Aurion Demo", layout="centered")
st.title("🔍 TruthMark-Aurion: Forensic Integrity Demo")

# Instructions and UI setup
st.markdown("""
### 👣 How to Use:
1. Upload baseline and subject videos.
2. Optionally use webcam input.
3. Click Run Forensic Validation below.
""")

# Sidebar uploads
baseline_video = st.sidebar.file_uploader("🎞️ Baseline Video", type=["mp4", "mov"])
subject_video = st.sidebar.file_uploader("📽️ Subject Video", type=["mp4", "mov"])
use_webcam = st.sidebar.checkbox("📷 Use Webcam for Subject Input")
if use_webcam and st.sidebar.button("Start Webcam Capture"):
    capture_webcam("uploads/webcam_input.mp4")
    st.sidebar.success("Webcam video saved.")

# ✅ Only now: Run validation button inside app flow
if st.button("Run Forensic Validation"):
    # Process inputs and render results
    ...
