import streamlit as st
import cv2
import tempfile
import time
import numpy as np
from fpdf import FPDF
from datetime import datetime
import matplotlib.pyplot as plt

# =============== PAGE CONFIG & STYLE ==============
st.set_page_config(page_title="TruthMark-Aurion", page_icon=":shield:", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #0d0d0d;
        color: #e6e6e6;
    }
    .css-1d391kg {background-color: #0d0d0d;}
    .css-1v3fvcr {color: #e6e6e6;}
    </style>
""", unsafe_allow_html=True)

# =============== HEADER & LOGO ==============
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>TruthMark-Aurion</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Guardian of the Truth</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #AAAAAA;'>Quantum Overseer</h4>", unsafe_allow_html=True)
st.markdown("---")

# =============== INPUT CHOICE: UPLOAD OR WEBCAM ==============
option = st.radio("Select input method:", ("Upload Video", "Use Webcam"))

video_file = None

if option == "Upload Video":
    video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])
elif option == "Use Webcam":
    if st.button("Record via Webcam"):
        cap = cv2.VideoCapture(0)
        frames = []
        st.info("Recording... Press 'Stop' to finish.")
        start_time = time.time()
        while time.time() - start_time < 5:  # record 5 seconds
            ret, frame = cap.read()
            if ret:
                frames.append(frame)
                st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        cap.release()
        temp_video = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
        height, width, _ = frames[0].shape
        out = cv2.VideoWriter(temp_video.name, cv2.VideoWriter_fourcc(*'mp4v'), 10, (width, height))
        for f in frames:
            out.write(f)
        out.release()
        video_file = temp_video

# =============== PROCESS THE VIDEO ==============
if video_file is not None:
    st.success("Video loaded. Starting forensic analysis...")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i+1)

    # ===== SAMPLE FOR DEMO: RANDOM GRAPH =====
    st.subheader("Forensic Signal Overview")
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    plt.figure()
    plt.plot(x, y)
    st.pyplot(plt)

    # ===== SAMPLE VERDICT =====
    st.markdown(f"""
        <div style='background-color:#1e1e1e; padding: 20px; border-radius: 10px; text-align: center;'>
        <h2 style='color:#00FFAA;'>Verdict: TRUTHFUL</h2>
        <p>Based on current biometric & linguistic indicators. (Simulated sample)</p>
        </div>
    """, unsafe_allow_html=True)

    # ===== PDF REPORT =====
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="TruthMark-Aurion Forensic Report", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
    pdf.cell(200, 10, txt="Verdict: TRUTHFUL (Sample)", ln=True, align='C')
    pdf_output = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(pdf_output.name)
    with open(pdf_output.name, "rb") as f:
        st.download_button("Download Forensic PDF Report", f, file_name="TruthMark-Aurion-Report.pdf")

# =============== FOOTER ==============
st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>© TruthMark-Aurion 2025 | Sebastian Andrews</p>", unsafe_allow_html=True)
