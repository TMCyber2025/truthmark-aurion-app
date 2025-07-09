import streamlit as st
import tempfile
import time
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# ===== CONFIG =====
st.set_page_config(page_title="TruthMark-Aurion", page_icon="🧬", layout="centered")

if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

# ===== CUSTOM CSS =====
st.markdown("""
<style>
    body { background-color: #0a0a0a; color: #e0e0e0; }
    .title {
        font-family: 'Courier New', monospace;
        font-size: 50px;
        color: #00f5d4;
        text-align: center;
        margin-top: 30px;
        text-shadow: 0 0 10px #00f5d4, 0 0 20px #00f5d4;
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #aaa;
        margin-bottom: 30px;
    }
    .hidden-input {
        visibility: hidden;
        height: 0;
        position: absolute;
    }
    .upload-area {
        border: 2px dashed #00f5d4;
        padding: 40px;
        border-radius: 15px;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s;
        margin: 0 auto;
        width: 90%;
        max-width: 450px;
    }
    .upload-area:hover {
        background-color: rgba(0,245,212,0.05);
        box-shadow: 0 0 20px #00f5d4;
    }
    .upload-text {
        font-size: 18px;
        color: #00f5d4;
    }
    .scanner {
        width: 100%;
        height: 12px;
        background: linear-gradient(90deg, transparent, #00f5d4, transparent);
        animation: scan 1.5s infinite linear;
        border-radius: 6px;
        margin: 20px 0;
    }
    @keyframes scan {
        0% { background-position: 0% }
        100% { background-position: 200% }
    }
    .verdict {
        background: #111;
        border: 1px solid #00f5d4;
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 0 20px #00f5d4;
    }
    .verdict h2 {
        color: #00f5d4;
        margin-bottom: 10px;
    }
    .verdict p {
        color: #ccc;
        font-size: 14px;
    }
    .footer {
        text-align: center;
        color: #666;
        font-size: 0.8em;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("<div class='title'>TruthMark-Aurion</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Quantum Multi-Modal Integrity Analysis</div>", unsafe_allow_html=True)

# ===== HIDDEN UPLOADER + STYLIZED DROP ZONE =====
st.markdown("<input type='file' class='hidden-input'>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["mp4", "mov", "avi"], label_visibility="collapsed")
st.markdown("""
<div class="upload-area" onclick="document.querySelector('input[type=file]').click()">
    <div class="upload-text">🧬 Drag & Drop Forensic File Here or Click to Browse</div>
    <div style='color:#aaa; font-size:13px;'>Accepted: .mp4, .mov, .avi</div>
</div>
""", unsafe_allow_html=True)

# ===== ANALYSIS SEQUENCE =====
if uploaded_file and not st.session_state.analysis_complete:
    st.video(uploaded_file)
    st.markdown("<div class='scanner'></div>", unsafe_allow_html=True)
    st.info("🧠 Initiating multi-layer biometric integrity scan...")

    logs = [
        "> Establishing subject baseline...",
        "> Calibrating micro-expression nodes...",
        "> Mapping neural temporal clusters...",
        "> Cross-referencing variance anomalies...",
        "> Synthesizing integrity matrix..."
    ]

    log_area = st.empty()
    likelihood_display = st.empty()
    likelihood = 0

    for i in range(100):
        time.sleep(0.03)

        if i % 20 == 0 and likelihood < 95:
            likelihood += 25
            likelihood_display.markdown(f"**Truth Likelihood:** {likelihood}%")

        if i // 20 < len(logs):
            log_area.markdown(logs[i // 20])

    likelihood_display.markdown("**Truth Likelihood:** 99.9%")
    log_area.markdown("> Analysis complete. Integrity stable.")
    st.session_state.analysis_complete = True

# ===== RESULTS =====
if st.session_state.analysis_complete:
    st.markdown("""
    <div class='verdict'>
        <h2>VERDICT: TRUTHFUL ✅</h2>
        <p>Signal integrity exceptionally high. No deception markers detected.</p>
        <p style='color:#f55'>⚠ Demo output. Not legally certified.</p>
    </div>
    """, unsafe_allow_html=True)

    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    plt.style.use('dark_background')
    plt.plot(x, y, color="#00f5d4", linewidth=2)
    plt.title("Neural Signal Trace", color="#ccc")
    st.pyplot(plt)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_output:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="TruthMark-Aurion | Integrity Report", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
        pdf.cell(200, 10, txt="Verdict: TRUTHFUL (Demo)", ln=True, align='C')
        pdf.output(pdf_output.name)
        with open(pdf_output.name, "rb") as f:
            st.download_button("📄 Download Integrity Report PDF", f, file_name="TruthMark-Aurion-Report.pdf")

# ===== FOOTER =====
st.markdown("<div class='footer'>TruthMark-Aurion © 2025 | Media encrypted & expunged post-analysis. Forensic chain simulated for demonstration.</div>", unsafe_allow_html=True)
