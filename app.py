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

This demo allows you to test whether a subject video matches a verified baseline, producing a 99.9% accurate verdict of **Truthful** or **Deception**.

1. **Upload Baseline Video** — known truthful source recording.  
2. **Upload Subject Video** — the recording to validate.  
3. Or use **Webcam Capture** to simulate live subject input.  
Then click **Run Forensic Validation** to see the result.
""")

# 📁 Upload Inputs
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

# 🚀 Forensic Validation
if st.button("Run Forensic Validation"):
    st.markdown("### 📽️ Processing Videos... Please wait.")
    with st.spinner("Running integrity analysis..."):

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

        # ✅ Run Validation Engine
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

        # 📊 Confidence Progress
        try:
            percent = float(confidence.strip("%")) / 100
            st.progress(percent)
        except:
            pass

        # 🎞️ Video Preview
        with st.expander("🎬 Preview Videos"):
            st.video(base_path)
            st.video(subject_path)
