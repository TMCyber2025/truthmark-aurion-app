# app.py
import streamlit as st
from engine import run_demo
from upload_webcam import capture_webcam
import os

# 🔧 Page setup
st.set_page_config(page_title="TruthMark-Aurion Demo", layout="centered")
st.title("🔍 TruthMark-Aurion: Forensic Integrity Demo")

# 📘 Instructions
st.markdown("""
### 👣 How to Use:
Upload a combined evidence video (including both baseline and subject) and a single metadata `.txt` file describing the context (timestamps, authorship notes, etc).  
Optionally, record a live webcam video for real-time validation.  
Then click **Run Forensic Validation** to generate results.
""")

# 📁 Upload Section
st.sidebar.header("📁 Upload Evidence")

combined_video = st.sidebar.file_uploader("🎞️ Combined Evidence Video", type=["mp4", "mov"])
evidence_txt = st.sidebar.file_uploader("📄 Evidence Metadata (.txt)", type=["txt"])

use_webcam = st.sidebar.checkbox("📷 Capture Webcam Input")
if use_webcam and st.sidebar.button("Start Webcam Capture"):
    capture_webcam("uploads/webcam_input.mp4")
    st.sidebar.success("Webcam video saved to uploads/webcam_input.mp4")

# 💡 File saving helper
def save_file(uploaded, path):
    with open(path, "wb") as f:
        f.write(uploaded.getbuffer())
    return path

# 🚀 Run Forensic Validation
if st.button("🔎 Run Forensic Validation"):
    with st.spinner("Validating evidence integrity..."):

        if combined_video and evidence_txt:
            video_path = save_file(combined_video, "data/combined_evidence.mp4")
            txt_path = save_file(evidence_txt, "data/evidence_notes.txt")

            result = run_demo(video_path, video_path, txt_path, txt_path)

            st.subheader("🧠 Integrity Assessment Result")
            st.json(result)

        elif use_webcam and os.path.exists("uploads/webcam_input.mp4") and evidence_txt:
            txt_path = save_file(evidence_txt, "data/evidence_notes.txt")

            result = run_demo("uploads/webcam_input.mp4", "uploads/webcam_input.mp4", txt_path, txt_path)

            st.subheader("🧠 Webcam Assessment Result")
            st.json(result)

        else:
            st.error("Please upload both a combined video and a metadata file, or use webcam with metadata.")
