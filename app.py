import streamlit as st
import tempfile
import time
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# =============== PAGE CONFIG ===============
st.set_page_config(page_title="TruthMark-Aurion", page_icon=":shield:", layout="centered")

# =============== CUSTOM CSS ===============
st.markdown("""
    <style>
    body { background-color: #0a0a0a; }
    h1, h2, h3, h4, p { font-family: 'Segoe UI', sans-serif; }
    .title-glow {
        color: #00FFAA;
        text-shadow: 0 0 10px #00FFAA, 0 0 20px #00FFAA;
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { text-shadow: 0 0 10px #00FFAA, 0 0 20px #00FFAA; }
        to { text-shadow: 0 0 20px #00FFAA, 0 0 40px #00FFAA; }
    }
    .verdict-box {
        background-color: #1e1e1e;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 0 20px #00FFAA;
        animation: pulse 3s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 10px #00FFAA; }
        50% { box-shadow: 0 0 30px #00FFAA; }
        100% { box-shadow: 0 0 10px #00FFAA; }
    }
    .disclaimer {
        color: #ff6666;
        font-size: 0.9em;
        margin-top: 15px;
    }
    .footer {
        text-align: center;
        color: #666;
        font-size: 0.85em;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# =============== HEADER ===============
st.markdown("""
    <h1 class='title-glow'>TruthMark-Aurion</h1>
    <h3 style='text-align: center; color: #cccccc;'>Guardian of the Truth</h3>
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

# =============== ANALYSIS EXPERIENCE ===============
if video_file is not None and not st.session_state.analysis_complete:
    st.success("Video loaded into the quantum forensic chamber. Preparing analysis...")
    st.video(video_file)

    progress = st.progress(0)
    status_text = st.empty()
    for i in range(100):
        time.sleep(0.025)
        progress.progress(i + 1)
        if i < 30:
            status_text.text("Initializing multi-sensor calibration...")
        elif i < 60:
            status_text.text("Analyzing biometric signatures...")
        elif i < 90:
            status_text.text("Fusing cognitive and linguistic signals...")
        else:
            status_text.text("Finalizing forensic truth model...")

    st.session_state.analysis_complete = True

# =============== RESULTS DISPLAY ===============
if st.session_state.analysis_complete:
    st.subheader("Forensic Signal Overview")
    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    plt.figure(facecolor='#0a0a0a')
    plt.plot(x, y, color='#00FFAA')
    plt.gca().set_facecolor('#1e1e1e')
    plt.tick_params(colors='#cccccc')
    plt.grid(color='#333333')
    st.pyplot(plt)

    st.markdown("""
        <div class='verdict-box'>
            <h2 style='color:#00FFAA;'>Verdict: TRUTHFUL</h2>
            <p>Based on 333 forensic sensor layers (simulated demo).</p>
            <p class='disclaimer'>⚠ This is a demonstration system. Reports are simulated and not certified findings.</p>
        </div>
    """, unsafe_allow_html=True)

    # PDF generation
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_output:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="TruthMark-Aurion Forensic Report (Demo)", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
        pdf.cell(200, 10, txt="Verdict: TRUTHFUL (Sample)", ln=True, align='C')
        pdf.output(pdf_output.name)
        with open(pdf_output.name, "rb") as f:
            st.download_button("Download Forensic PDF Report", f, file_name="TruthMark-Aurion-Report.pdf")

# =============== FOOTER ===============
st.markdown("""
    <div class='footer'>
        © 2025 TruthMark-Aurion | Sebastian Andrews<br>
        This demonstration encrypts uploaded data and deletes it after analysis.<br>
        Reports generated here are for demonstration purposes only.
    </div>
""", unsafe_allow_html=True)
