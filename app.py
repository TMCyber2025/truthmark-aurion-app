import streamlit as st
import tempfile
import time
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# === CONFIG ===
st.set_page_config(page_title="TruthMark-Aurion", layout="centered")

if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

# === CLEAN CSS ===
st.markdown("""
<style>
    body { background-color: #eaf2fb; color: #1b1e23; font-family: 'Segoe UI', sans-serif; }
    h1, h2 { text-align: center; color: #0c4a7d; }
    .header { padding-top: 20px; }
    .upload-box {
        border: 2px dashed #0c4a7d;
        background-color: #f2f7fc;
        padding: 30px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        transition: box-shadow 0.3s ease-in-out;
    }
    .upload-box:hover {
        box-shadow: 0 0 15px #91c2e3;
    }
    .scanner-bar {
        height: 10px;
        width: 100%;
        background: linear-gradient(90deg, #91c2e3, #0c4a7d);
        background-size: 200% 100%;
        animation: scan 1.5s infinite linear;
        border-radius: 5px;
        margin: 20px 0;
    }
    @keyframes scan {
        0% { background-position: 0% }
        100% { background-position: 200% }
    }
    .verdict-box {
        background-color: #d8e6f2;
        border-left: 6px solid #0c4a7d;
        padding: 20px;
        border-radius: 8px;
        margin-top: 30px;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        color: #555;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown("<div class='header'><h1>TruthMark-Aurion</h1><h2>Biometric Integrity Lab</h2></div>", unsafe_allow_html=True)

# === FILE UPLOAD ===
uploaded_file = st.file_uploader("", type=["mp4", "mov", "avi"], label_visibility="collapsed")
st.markdown("<div class='upload-box'>🧬 Drag & Drop Forensic Footage Here<br><small>Accepted formats: .mp4 | .mov | .avi</small></div>", unsafe_allow_html=True)

# === SCAN SEQUENCE ===
if uploaded_file and not st.session_state.analysis_complete:
    st.video(uploaded_file)
    st.markdown("<div class='scanner-bar'></div>", unsafe_allow_html=True)
    st.info("Running biometric signal clustering algorithm...")

    logs = [
        "▶ Initializing sensor matrix...",
        "▶ Capturing micro-expression data...",
        "▶ Evaluating linguistic cadence...",
        "▶ Matching profiles against truth vector...",
        "▶ Consolidating integrity output..."
    ]

    log_area = st.empty()
    likelihood_display = st.empty()
    likelihood = 0

    for i in range(100):
        time.sleep(0.02)
        if i % 20 == 0 and likelihood < 95:
            likelihood += 25
            likelihood_display.markdown(f"**Signal Confidence:** {likelihood}%")
        if i // 20 < len(logs):
            log_area.markdown(logs[i // 20])

    likelihood_display.markdown("**Signal Confidence:** 99.9%")
    log_area.markdown("✔️ Scan complete. No anomaly detected.")
    st.session_state.analysis_complete = True

# === VERDICT OUTPUT ===
if st.session_state.analysis_complete:
    st.markdown("""
    <div class='verdict-box'>
        <h2>Verdict: TRUTHFUL</h2>
        <p>Biometric readings consistent with expected baselines.</p>
        <p style='color:#a00; font-size: 12px;'>⚠ This report is a demonstration and not legally certified.</p>
    </div>
    """, unsafe_allow_html=True)

    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    plt.style.use('seaborn-whitegrid')
    plt.plot(x, y, color="#0c4a7d", linewidth=2)
    plt.title("Signal Trace Map", color="#0c4a7d")
    st.pyplot(plt)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_output:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="TruthMark-Aurion | Integrity Report", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
        pdf.cell(200, 10, txt="Verdict: TRUTHFUL (Demo)", ln=True, align='C')
        pdf.output(pdf_output.name)
        with open(pdf_output.name, "rb") as f:
            st.download_button("Download PDF Report", f, file_name="TruthMark-Aurion-Report.pdf")

# === FOOTER ===
st.markdown("<div class='footer'>TruthMark-Aurion © 2025 | Demo mode active. Media purged post-analysis.</div>", unsafe_allow_html=True)
