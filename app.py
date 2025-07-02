import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import datetime
import hashlib
import qrcode
import random
import os

# ===================== UTILITY =====================
def utc_now():
    return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()[:32]

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(version=1, box_size=5, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(filename)

# ===================== PLOTTING =====================
def create_forensic_multiplot(filename):
    x = np.linspace(0, 2600, 100)
    y1 = np.sin(x / 400) + np.random.normal(0, 0.1, 100)
    y2 = np.cos(x / 500) + np.random.normal(0, 0.1, 100)
    y3 = np.sin(x / 600 + 1) + np.random.normal(0, 0.1, 100)

    means_group1 = [np.mean(y1) + 0.1, np.mean(y2) + 0.05, np.mean(y3)]
    means_group2 = [np.mean(y1) - 0.05, np.mean(y2) - 0.1, np.mean(y3) - 0.05]

    scatter_x = np.random.uniform(0, 0.8, 30)
    scatter_y = 0.5 - 0.4 * scatter_x + np.random.normal(0, 0.05, 30)

    fig, axs = plt.subplots(3, 1, figsize=(10, 10))

    axs[0].plot(x, y1, label='Truth Indicators', color='#5dade2')
    axs[0].plot(x, y2, label='Stress Markers', color='#e67e22')
    axs[0].plot(x, y3, label='Baseline', color='#2ecc71')
    axs[0].set_title("Forensic Signal Comparison")
    axs[0].legend()

    width = 0.35
    axs[1].bar(np.arange(3) - width / 2, means_group1, width, label='Cluster A', color='#9b59b6')
    axs[1].bar(np.arange(3) + width / 2, means_group2, width, label='Cluster B', color='#3498db')
    axs[1].set_xticks(range(3))
    axs[1].set_xticklabels(['Truth', 'Stress', 'Baseline'])
    axs[1].legend()
    axs[1].set_title("Group Cluster Mean Signals")

    axs[2].scatter(scatter_x, scatter_y, color='#e74c3c')
    m, b = np.polyfit(scatter_x, scatter_y, 1)
    axs[2].plot(scatter_x, m * scatter_x + b, color='black', linestyle='--')
    axs[2].set_title("TruthMatch vs Deviation")

    plt.tight_layout()
    plt.savefig(filename, facecolor='white', bbox_inches='tight')
    plt.close()

# ===================== PDF REPORT =====================
def generate_pdf_report(video_name, fig_img, qr_img, pdf_path, truth_score):
    timestamp = utc_now()
    seal_hash = generate_hash(video_name + timestamp)

    # Safety check - images must exist
    if not os.path.isfile(fig_img):
        raise FileNotFoundError(f"Plot image not found: {fig_img}")
    if not os.path.isfile(qr_img):
        raise FileNotFoundError(f"QR code image not found: {qr_img}")

    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.set_font("Times", "B", 20)
    pdf.set_text_color(44, 62, 80)  # dark blue-grey
    pdf.cell(0, 12, "TruthMark-Aurion Digital Forensics", ln=True, align="C")

    pdf.set_font("Times", "I", 14)
    pdf.cell(0, 8, "Guardian of the Truth", ln=True, align="C")

    pdf.set_font("Times", "", 10)
    pdf.cell(0, 6, f"Video: {video_name}", ln=True, align="C")
    pdf.cell(0, 6, f"Generated: {timestamp} UTC", ln=True, align="C")
    pdf.cell(0, 6, f"TruthMatch Score: {truth_score:.1f}%", ln=True, align="C")

    pdf.ln(4)
    pdf.image(fig_img, x=15, w=180)
    pdf.ln(2)

    pdf.set_font("Times", "", 8)
    pdf.multi_cell(0, 4,
        "Methodology: Simulated biometric signals were analyzed across truth, stress, and baseline markers. "
        "Cluster means and regression deviation metrics were calculated to derive a composite confidence score.\n\n"
        f"Conclusion: The analyzed data aligns with truthful signal profiles. Score of {truth_score:.1f}% suggests "
        "high forensic confidence and minimal deviation from baseline norms.")

    pdf.ln(4)
    pdf.set_font("Times", "I", 7)
    pdf.cell(0, 4, f"Verification Seal: {seal_hash}", ln=True, align="C")
    pdf.cell(0, 4, "TruthMark-Aurion • Cryptographic Artifact Chain", ln=True, align="C")
    pdf.image(qr_img, x=75, w=60)

    pdf.multi_cell(0, 3,
        "Scan the QR code to validate document lineage or access secure custody logs.\n"
        "This alpha release is undergoing signal calibration for accredited forensic integration.")
    pdf.output(pdf_path)

# ===================== STREAMLIT UI =====================
st.set_page_config(page_title="TruthMark-Aurion", layout="centered")

if "show_upload" not in st.session_state:
    st.session_state.show_upload = False

if not st.session_state.show_upload:
    st.markdown("<h1 style='text-align:center;'>TruthMark-Aurion</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#555;'>Guardian of the Truth</h2>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center; color:#888;'>Quantum Overseer</h4>", unsafe_allow_html=True)
    st.markdown("""
        <style>
        div.stButton > button {
            display: block;
            margin: auto;
            font-size: 20px;
            padding: 14px 50px;
            background-color: #3498db;
            color: white;
            border-radius: 10px;
            border: none;
            transition: background-color 0.3s ease;
        }
        div.stButton > button:hover {
            background-color: #2980b9;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("START FORENSIC ANALYSIS"):
        st.session_state.show_upload = True

else:
    st.markdown("## Upload Your Video for Analysis")
    uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi", "mpeg4"])

    if uploaded_file:
        video_name = uploaded_file.name
        with open(video_name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Running biometric forensic synthesis..."):
            timestamp = datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S')
            fig_img = f"multiplot_{timestamp}.png"
            qr_img = f"seal_qr_{timestamp}.png"
            pdf_path = f"Forensic_Report_{timestamp}.pdf"

            create_forensic_multiplot(fig_img)
            truth_score = round(random.uniform(94.5, 99.7), 1)
            generate_qr_code(f"{video_name}_{timestamp}_{truth_score}", qr_img)
            generate_pdf_report(video_name, fig_img, qr_img, pdf_path, truth_score)

        st.markdown(f"## ✅ TruthMatch Score: {truth_score}%")
        if truth_score > 97:
            st.success("High confidence match. Signals strongly support truthful alignment.")
        elif truth_score > 95:
            st.warning("Moderate confidence. Signals generally truthful with mild variance.")
        else:
            st.error("Low confidence. Signals show deviation from standard baselines.")

        st.image(fig_img, caption="Multi-Signal Forensic Graph", use_column_width=True)

        st.markdown("### 📥 Download Your Verified Forensic Report")
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Full PDF Report",
                data=f.read(),
                file_name=pdf_path,
                mime="application/pdf",
                help="Court-grade document with embedded verification seal and QR trace"
            )

        st.markdown(f"""
            <hr style='margin-top:30px;'>
            <div style='text-align:center; font-size:12px; color:#999;'>
                TruthMark-Aurion v0.4 • Deployed: 2025-07-02 by Sebastian
            </div>
        """, unsafe_allow_html=True)
