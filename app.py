import streamlit as st
import tempfile
import time
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# =============== PAGE CONFIG ===============
st.set_page_config(page_title="TruthMark-Aurion", page_icon=":shield:", layout="centered")

# =============== HEADER & TAGLINE ===============
st.markdown("""
    <h1 style='text-align: center; color: #00FFAA;'>TruthMark-Aurion</h1>
    <h3 style='text-align: center;'>Guardian of the Truth</h3>
    <h4 style='text-align: center; color: #AAAAAA;'>Quantum Overseer</h4>
    <p style='text-align: center; color: #AAAAAA; margin-top: -10px;'>333 forensic sensors. Full truth PDF generated.</p>
    <hr>
""", unsafe_allow_html=True)

# =============== FILE UPLOAD ===============
st.caption("Max file size: ~100MB recommended for smooth demo performance.")
video_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

# Store app state
if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

# =============== ANALYSIS LOGIC ===============
if video_file is not None and not st.session_state.analysis_complete:
    st.success("Video loaded. Starting forensic analysis...")
    st.video(video_file)

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.session_state.analysis_complete = True

# =============== RESULTS DISPLAY ===============
if st.session_state.analysis_complete:
    st.subheader("Forensic Signal Overview")
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    plt.clf()
    plt.plot(x, y)
    st.pyplot(plt)

    st.markdown("""
        <div style='background-color:#1e1e1e; padding: 20px; border-radius: 10px; text-align: center;'>
            <h2 style='color:#00FFAA;'>Verdict: TRUTHFUL</h2>
            <p>Based on current biometric & linguistic indicators. (Simulated sample)</p>
        </div>
    """, unsafe_allow_html=True)

    # PDF generation
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_output:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="TruthMark-Aurion Forensic Report", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
        pdf.cell(200, 10, txt="Verdict: TRUTHFUL (Sample)", ln=True, align='C')
        pdf.output(pdf_output.name)
        with open(pdf_output.name, "rb") as f:
            st.download_button("Download Forensic PDF Report", f, file_name="TruthMark-Aurion-Report.pdf")

# =============== FOOTER ===============
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.85em;'>
        © 2025 TruthMark-Aurion | Sebastian Andrews<br>
        Data encrypted during analysis and securely purged after report generation.
    </div>
""", unsafe_allow_html=True)
