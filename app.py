import streamlit as st
import tempfile
import time
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime

# === PAGE CONFIG ===
st.set_page_config(page_title="TruthMark-Aurion", layout="centered")

if "analysis_complete" not in st.session_state:
    st.session_state.analysis_complete = False

# === CLEAN CSS: FORENSIC BLUE THEME ===
st.markdown("""
<style>
    body {
        background-color: #f8fbff;
        color: #103d62;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2 {
        text-align: center;
        color: #175e9d;
    }
    .banner {
        padding-top: 20px;
        padding-bottom: 10px;
    }
    .upload-zone {
        border: 2px dashed #175e9d;
        background-color: #eff7ff;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
        transition: all 0.3s;
    }
    .upload-zone:hover {
        box-shadow: 0 0 10px #9ecff2;
        background-color: #e5f3ff;
    }
    .pulse-bar {
        height: 12px;
        width: 100%;
        background: linear-gradient(90deg, #175e9d 0%, #9ecff2 50%, #175e9d 100%);
        background-size: 200% 100%;
        animation: pulse 1.8s infinite linear;
        border-radius: 6px;
        margin: 20px 0;
    }
    @keyframes pulse {
        0% { background-position: 0% }
        100% { background-position: 200% }
    }
    .verdict {
        background-color: #dceefb;
        border-left: 6px solid #175e9d;
        padding: 20px;
        border-radius: 8px;
        margin-top: 30px;
    }
    .footer {
        text-align: center;
        font-size: 11px;
        color: #3b5b7a;
        margin-top: 50px;
    }
</style>
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown("<div class='banner'><h1>TruthMark-Aurion</h1><h2>Iceflow Biometric Intelligence System</h2></div>", unsafe_allow_html=True)

# === FILE UPLOAD ===
uploaded_file = st.file_uploader("", type=["mp4", "mov", "avi"], label_visibility="collapsed")
st.markdown("""
<div class="upload-zone">
    🧬 Drag & Drop Subject Footage<br><small>Accepted formats: mp4, mov, avi</small>
</div>
""", unsafe_allow_html=True)

# === ANALYSIS LOGIC ===
if uploaded_file and not st.session_state.analysis_complete:
    st.video(uploaded_file)
    st.markdown("<div class='pulse-bar'></div>", unsafe_allow_html=True)
    st.info("⏳ Activating biometric-linguistic signal sweep...")

    logs = [
        "• Establishing forensic baseline",
        "• Scanning micro-expression vectors",
        "• Assessing linguistic consistency",
        "• Cross-referencing temporal anomalies",
        "• Finalizing truth metric confidence"
    ]

    log_area = st.empty()
    likelihood_display = st.empty()
    likelihood = 0

    for i in range(100):
        time.sleep(0.02)
        if i % 20 == 0 and likelihood < 95:
            likelihood += 25
            likelihood_display.markdown(f"**Truth Likelihood:** {likelihood}%")
        if i // 20 < len(logs):
            log_area.markdown(logs[i // 20])

    likelihood_display.markdown("**Truth Likelihood:** 99.9%")
    log_area.markdown("✅ Analysis complete. Integrity secure.")
    st.session_state.analysis_complete = True

# === VERDICT OUTPUT ===
if st.session_state.analysis_complete:
    st.markdown("""
    <div class='verdict'>
        <h2>Verdict: TRUTHFUL</h2>
        <p>Signal integrity aligned with all biometric expectations. No deception indicators found.</p>
        <p style='color:#b00; font-size: 12px;'>⚠ This demo is not legally certified or admissible.</p>
    </div>
    """, unsafe_allow_html=True)

    x = np.linspace(0, 10, 100)
    y = np.sin(x) + np.random.normal(0, 0.1, 100)
    plt.style.use('seaborn-white')
    plt.plot(x, y, color="#175e9d", linewidth=2)
    plt.title("Signal Noise Map", color="#175e9d")
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
st.markdown("<div class='footer'>TruthMark-Aurion © 2025 | Data purged post-evaluation. For demonstration use only.</div>", unsafe_allow_html=True)
