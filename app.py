import streamlit as st
import tempfile
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime
from engine import analyze_with_baseline

# Streamlit config
st.set_page_config(page_title="TruthMark-Aurion", page_icon="🧬", layout="centered")

# Branding
st.markdown("""
<style>
body { background-color: #f8f9fa; color: #333; }
.title { font-family: 'Courier New'; font-size: 48px; color: #00c9a7; text-align: center; margin-top: 30px; }
.subtitle { text-align: center; font-size: 20px; color: #555; margin-bottom: 30px; }
.footer { text-align: center; color: #777; font-size: 0.85em; margin-top: 40px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>TruthMark-Aurion</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Comparative Biometric-Linguistic Integrity Check</div>", unsafe_allow_html=True)

# File uploads
baseline_video = st.file_uploader("🧬 Upload Baseline Video", type=["mp4", "mov", "avi"])
subject_video = st.file_uploader("🎥 Upload Subject Video", type=["mp4", "mov", "avi"])
st.markdown("---")

# Run analysis if both videos are uploaded
if baseline_video and subject_video:
    st.video(baseline_video, format="video/mp4", start_time=0)
    st.video(subject_video, format="video/mp4", start_time=0)
    st.info("🔍 Comparing biometric signals and audio features...")

    results = analyze_with_baseline(baseline_video, subject_video)

    st.success(f"✅ Verdict: {results['verdict']}")
    st.write(f"📍 Timestamp: {results['timestamp']}")
    st.write(f"💓 HRV Difference: {results['hrv_delta']}")
    st.write(f"👁️ Blink Rate Difference: {results['blink_delta']}")
    st.write(f"🧠 Semantic Drift (MFCC Cosine Distance): {results['drift_score']}")

    # Plot rPPG and EAR traces side-by-side
    fig, ax = plt.subplots()
    ax.plot(results["rppg_curves"]["baseline"], label="Baseline rPPG", color="#00c9a7")
    ax.plot(results["rppg_curves"]["subject"], label="Subject rPPG", color="#004466", linestyle="--")
    ax.set_title("rPPG Signal Comparison")
    ax.legend(); ax.grid()
    st.pyplot(fig)

    fig2, ax2 = plt.subplots()
    ax2.plot(results["ear_curves"]["baseline"], label="Baseline EAR", color="#ff7f50")
    ax2.plot(results["ear_curves"]["subject"], label="Subject EAR", color="#993333", linestyle="--")
    ax2.set_title("Blink/EAR Comparison")
    ax2.legend(); ax2.grid()
    st.pyplot(fig2)

    # PDF Report
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_output:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="TruthMark-Aurion | Comparative Report", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Timestamp: {results['timestamp']}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Verdict: {results['verdict']}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"HRV Delta: {results['hrv_delta']}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Blink Rate Delta: {results['blink_delta']}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Semantic Drift Score: {results['drift_score']}", ln=True, align='C')
        pdf.output(pdf_output.name)
        with open(pdf_output.name, "rb") as f:
            st.download_button("📄 Download Comparative Report", f, file_name="TruthMark-Aurion-Comparison.pdf")

st.markdown("<div class='footer'>TruthMark-Aurion © 2025 | Baseline and subject videos analyzed via rPPG, EAR, and MFCC feature comparison. Verdict based on biometric integrity deviations.</div>", unsafe_allow_html=True)
