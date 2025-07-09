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

# === HEADER ===
st.markdown("""
    <style>
        body { background-color: #f5f5f5; color: #222; font-family: Arial, sans-serif; }
        h1, h2, h3 { text-align: center; color: #333; }
        .section { padding: 20px; margin-top: 20px; border: 1px solid #ddd; border-radius: 8px; background-color: #fff; }
        .log { font-family: monospace; font-size: 14px; background-color: #eee; padding: 10px; border-radius: 5px; }
        .footer { text-align: center; font-size: 11px; color: #666; margin-top: 50px; }
        .button { background-color: #004080; color: white; padding: 10px 20px; border-radius: 5px; text-align: center; }
    </style>
    <h1>TruthMark-Aurion</h1>
    <h3>Multi-Modal Integrity Scanner</h3>
""", unsafe_allow_html=True)

# === FILE UPLOAD ===
st.markdown("<div class='section'><h2>Upload Evidence File</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Accepted formats: .mp4, .mov, .avi", type=["mp4", "mov", "avi"])
st.markdown("</div>", unsafe_allow_html=True)

# === ANALYSIS SEQUENCE ===
if uploaded_file and not st.session_state.analysis_complete:
    st.markdown("<div class='section'><h2>Initial Scan Protocol</h2>", unsafe_allow_html=True)
    st.video(uploaded_file)

    logs = [
        ">> Secure timestamp generation...",
        ">> Normalizing biometric patterns...",
        ">> Extracting linguistic rhythm...",
        ">> Comparing against known anomaly signatures...",
        ">> Constructing final integrity verdict..."
    ]

    log_area = st.empty()
    likelihood_display = st.empty()
    likelihood = 0

    for i in range(100):
        time.sleep(0.02)
        if i % 20 == 0 and likelihood < 95:
            likelihood += 25
            likelihood_display.markdown(f"**Truth Confidence:** {likelihood}%")
        if i // 20 < len(logs):
            log_area.markdown(f"<div class='log'>{logs[i // 20]}</div>", unsafe_allow_html=True)

    likelihood_display.markdown("**Truth Confidence:** 99.9%")
    log_area.markdown("<div class='log'>>> Scan complete. No anomalies detected.</div>", unsafe_allow_html=True)
    st.session_state.analysis_complete = True
    st.markdown("</div>", unsafe_allow_html=True)

# === OUTPUT ===
if st.session_state.analysis_complete:
    st.markdown("<div class='section'><h2>Signal Verdict</h2>", unsafe_allow_html=True)
    st.markdown("""
        <h3 style='text-align: center; color: green;'>VERDICT: TRUTHFUL</h3>
        <p style='text-align: center; color: #444;'>No biometric deviation or linguistic conflict detected. Signal integrity stable.</p>
        <p style='text-align: center; font-size: 12px; color: red;'>⚠ For demonstration purposes only. Not court-certified.</p>
    """, unsafe_allow_html=True)

    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    plt.style.use('ggplot')
    plt.plot(x, y, color="black")
    plt.title("Biometric Noise Signature")
    st.pyplot(plt)
    st.markdown("</div>", unsafe_allow_html=True)

    # === PDF Output ===
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_output:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="TruthMark-Aurion | Report Summary", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align='C')
        pdf.cell(200, 10, txt="Verdict: TRUTHFUL (Demo)", ln=True, align='C')
        pdf.output(pdf_output.name)
        with open(pdf_output.name, "rb") as f:
            st.download_button("Download PDF Report", f, file_name="Aurion-Report.pdf")

# === FOOTER ===
st.markdown("""
<div class='footer'>
    TruthMark-Aurion © 2025 | Report simulated for integrity demonstration only.<br>
    All uploads anonymized and purged. Legal deployment requires certified authority.
</div>
""", unsafe_allow_html=True)
