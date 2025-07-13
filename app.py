import streamlit as st
import tempfile
import matplotlib.pyplot as plt
from fpdf import FPDF
from datetime import datetime
from engine import analyze_evidence

st.set_page_config(page_title="TruthMark-Aurion", page_icon="🧬", layout="centered")

st.markdown("""
<style>
body { background-color: #f8f9fa; color: #333; }
.title { font-family: 'Courier New'; font-size: 48px; color: #00c9a7; text-align: center; margin-top: 30px; }
.subtitle { text-align: center; font-size: 20px; color: #555; margin-bottom: 30px; }
.footer { text-align: center; color: #777; font-size: 0.85em; margin-top: 40px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>TruthMark-Aurion</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Biometric-Linguistic Forensic Analysis</div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("🎥 Upload Video File", type=["mp4", "mov", "avi"])
baseline_file = st.file_uploader("📄 Upload Baseline Transcript (TXT)", type=["txt"])

st.markdown("---")

if uploaded_file and baseline_file:
    st.video(uploaded_file)
    with baseline_file as f:
        baseline_text = f.read().decode("utf-8")

    st.info("🔍 Running biometric and linguistic scoring...")
    results = analyze_evidence(uploaded_file, baseline_text)

    st.success(f"✅ Verdict: {results['verdict']}")
    st.write(f"📍 Timestamp: {results['timestamp']}")
    st.write(f"💓 Heart Rate: {results['heart_rate']} bpm")
    st.write(f"📈 HRV Std Dev: {results['hrv_std']}")
    st.write(f"👁️ Blink EAR: {results['blink_ear']}")
    st.write(f"🧠 Semantic Drift Score: {results['drift_score']}")

    fig, ax = plt.subplots()
    ax.plot(results['rppg_curve'], label="rPPG", color="#00c9a7")
    ax.plot(results['ear_curve'], label="EAR", color="#ff7f50")
    ax.set_title("Biometric Signal Trace")
    ax.legend(); ax.grid()
    st.pyplot(fig)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_output:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="TruthMark-Aurion | Integrity Report", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Timestamp: {results['timestamp']}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Verdict: {results['verdict']}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Heart Rate: {results['heart_rate']} bpm", ln=True, align='C')
        pdf.cell(200, 10, txt=f"HRV Std Dev: {results['hrv_std']}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Blink EAR: {results['blink_ear']}", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Semantic Drift: {results['drift_score']}", ln=True, align='C')
        pdf.output(pdf_output.name)
        with open(pdf_output.name, "rb") as f:
            st.download_button("📄 Download Integrity Report PDF", f, file_name="TruthMark-Aurion-Report.pdf")

st.markdown("<div class='footer'>TruthMark-Aurion © 2025 | Forensic report generated based on uploaded media and comparative context.</div>", unsafe_allow_html=True)
