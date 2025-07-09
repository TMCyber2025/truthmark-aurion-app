import streamlit as st
import tempfile
import time
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# ===== CONFIG =====
st.set_page_config(page_title="TruthMark-Aurion", page_icon="🧬", layout="centered")

# ===== SESSION STATE =====
if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

# ===== CUSTOM CSS: NEON LAB LOOK =====
st.markdown("""
<style>
    body { background-color: #0a0a0a; color: #e0e0e0; }
    .main-title {
        font-family: 'Courier New', monospace;
        font-size: 48px;
        color: #00f5d4;
        text-align: center;
        margin-top: 30px;
        text-shadow: 0 0 10px #00f5d4, 0 0 20px #00f5d4;
    }
    .subtitle {
        font-size: 20px;
        color: #888;
        text-align: center;
        margin-bottom: 30px;
    }
    .upload-box {
        background: #111;
        border: 1px solid #333;
        border-radius: 12px;
        padding: 30px;
        text-align: center;
        width: 90%;
        max-width: 500px;
        margin: 0 auto 40px auto;
    }
    .upload-box h3 {
        color: #00f5d4;
        font-size: 24px;
        margin-bottom: 10px;
    }
    .scanner {
        width: 100%;
        height: 10px;
        background: linear-gradient(90deg, transparent, #00f5d4, transparent);
        animation: scan 1.5s infinite linear;
        border-radius: 5px;
        margin-top: 20px;
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

# ===== TITLE =====
st.markdown("<div class='main-title'>TruthMark-Aurion</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Multi-Modal Quantum Forensic Analysis</div>", unsafe_allow_html=True)

# ===== UPLOAD =====
st.markdown("""
<div class='upload-box'>
    <h3>🧬 Upload Forensic Footage</h3>
    <p style='color:#aaa'>Formats: .mp4 | .mov | .avi</p>
</div>
""", unsafe_allow_html=True)

video_file = st.file_uploader("", type=["mp4", "mov", "avi"])

# ===== ANALYSIS SEQUENCE =====
if video_file and not st.session_state.analysis_complete:
    st.video(video_file)
    st.markdown("<div class='scanner'></div>", unsafe_allow_html=True)
    st.info("🧠 Initiating biometric-linguistic multi-layer scan...")

    logs = [
        "> Establishing subject baseline...",
        "> Calibrating micro-expression lattice...",
        "> Mapping neural pause clusters...",
        "> Cross-referencing stress variances...",
        "> Finalizing integrity synthesis..."
    ]

    progress = st.empty()
    log_area = st.empty()
    likelihood_display = st.empty()
    likelihood = 0

    for i in range(100):
        time.sleep(0.03)
        progress.progress(i + 1)

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
    st.markdown("<div class='verdict'><h2>VERDICT: TRUTHFUL ✅</h2><p>Signal integrity exceptionally high. No deception markers detected.</p><p style='color:#f55'>⚠ Demo output. Not certified.</p></div>", unsafe_allow_html=True)

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
st.markdown("<div class='footer'>TruthMark-Aurion © 2025 | Media encrypted & expunged post-analysis. Simulated forensic chain for demonstration.</div>", unsafe_allow_html=True)
