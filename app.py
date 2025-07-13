# app.py
import streamlit as st
from engine import run_demo
from upload_webcam import capture_webcam
import os

# 🔧 Page Setup
st.set_page_config(page_title="TruthMark-Aurion Demo", layout="centered")
st.title("🔍 TruthMark-Aurion: Forensic Integrity Demo")

# 📘 Instructions
st.markdown("""
### 👣 How to Use:
1. **Upload Baseline Video** – verified source material.  
2. **Upload Subject Video** – evidence input to validate.  
3. Or toggle **webcam** to simulate live input.  
Click **Run Forensic Validation** to assess integrity and detect anomalies.
""")

# 📁 Sidebar Uploads
st.sidebar.header("📁 Upload Inputs")

baseline_video = st.sidebar.file_uploader("🎞️ Baseline Video", type=["mp4", "mov"], key="baseline")
subject_video = st.sidebar.file_uploader("📽️ Subject Video", type=["mp4", "mov"], key="subject")

use_webcam = st.sidebar.checkbox("📷 Use Webcam for Subject Input")
if use_webcam and st.sidebar.button("Start Webcam Capture"):
    capture_webcam("uploads/webcam_input.mp4")
    st.sidebar.success("Webcam video saved to uploads/webcam_input.mp4")

# 💾 File Saver
def save_file(uploaded, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(uploaded.getbuffer())
    return path

# 🚀 Run Validation
if st.button("Run Forensic Validation"):
    with st.spinner("Running integrity analysis..."):

        # ✅ Validate baseline upload
        if baseline_video is not None:
            base_path = save_file(baseline_video, "data/baseline.mp4")
        else:
            st.error("❌ Please upload a Baseline Video.")
            st.stop()

        # ✅ Validate subject input (webcam or file)
        if use_webcam and os.path.exists("uploads/webcam_input.mp4"):
            subject_path = "uploads/webcam_input.mp4"
        elif subject_video is not None:
            subject_path = save_file(subject_video, "data/subject.mp4")
        else:
            st.error("❌ Please upload a Subject Video or use Webcam.")
            st.stop()

        # ✅ Run Demo
        result = run_demo(base_path, subject_path, "", "")
        st.subheader("🧠 Validation Result")
        st.json(result)
