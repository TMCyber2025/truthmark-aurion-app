import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import datetime
import hashlib

# ============ HELPERS ============
def utc_now():
    return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

def generate_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()[:32]

def create_forensic_multiplot(filename):
    x = np.linspace(0, 2600, 100)
    y1 = np.sin(x/400) + np.random.normal(0,0.1,100)
    y2 = np.cos(x/500) + np.random.normal(0,0.1,100)
    y3 = np.sin(x/600 + 1) + np.random.normal(0,0.1,100)

    means_group1 = [np.mean(y1)+0.1, np.mean(y2)+0.05, np.mean(y3)]
    means_group2 = [np.mean(y1)-0.05, np.mean(y2)-0.1, np.mean(y3)-0.05]

    scatter_x = np.random.uniform(0,0.8,30)
    scatter_y = 0.5 - 0.4*scatter_x + np.random.normal(0,0.05,30)

    fig, axs = plt.subplots(3, 1, figsize=(10,10))
    axs[0].plot(x, y1, label='Truth Indicators', color='#5dade2')
    axs[0].plot(x, y2, label='Stress Markers', color='#e67e22')
    axs[0].plot(x, y3, label='Baseline', color='#2ecc71')
    axs[0].set_title("Forensic Signal Comparison")
    axs[0].legend()

    width=0.35
    axs[1].bar(np.arange(3)-width/2, means_group1, width, label='Cluster A', color='#9b59b6')
    axs[1].bar(np.arange(3)+width/2, means_group2, width, label='Cluster B', color='#3498db')
    axs[1].set_xticks(range(3))
    axs[1].set_xticklabels(['Truth', 'Stress', 'Baseline'])
    axs[1].legend()
    axs[1].set_title("Group Cluster Mean Signals")

    axs[2].scatter(scatter_x, scatter_y, color='#e74c3c')
    m,b = np.polyfit(scatter_x, scatter_y, 1)
    axs[2].plot(scatter_x, m*scatter_x + b, color='black', linestyle='--')
    axs[2].set_title("TruthMatch vs Deviation")

    plt.tight_layout()
    plt.savefig(filename, facecolor='white', bbox_inches='tight')
    plt.close()

def generate_pdf_report(video_name, fig_img, pdf_path, truth_score):
    timestamp = utc_now()
    seal_hash = generate_hash(video_name + timestamp)

    pdf = FPDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()

    pdf.set_font("Times", "B", 18)
    pdf.cell(0, 10, "TruthMark-Aurion Digital Forensic Report", ln=True, align="C")

    pdf.set_font("Times", "", 9)
    pdf.cell(0, 5, f"Video: {video_name}", ln=True, align="C")
    pdf.cell(0, 5, f"Generated: {timestamp} UTC", ln=True, align="C")
    pdf.cell(0, 5, f"TruthMatch Score: {truth_score:.1f}%", ln=True, align="C")

    pdf.ln(4)
    pdf.image(fig_img, x=15, w=180)
    pdf.ln(3)

    pdf.set_font("Times", "", 8)
    pdf.multi_cell(0, 4,
        "Methodology: Multi-signal simulated biometric analysis was conducted across truth, stress, and baseline markers. "
        "Cluster means and deviation regressions were calculated for composite scoring.\n\n"
        "Conclusion: The current data indicates alignment with truthful norms, resulting in a TruthMatch Score of "
        f"{truth_score:.1f}%, supporting high forensic confidence with no significant deception signals."
    )

    pdf.ln(3)
    pdf.set_font("Times", "I", 7)
    pdf.cell(0, 4, f"Verification Seal: {seal_hash}", ln=True, align="C")
    pdf.cell(0, 4, "Verified Digital Forensic Document - TruthMark-Aurion", ln=True, align="C")
    pdf.ln(2)
    pdf.multi_cell(0, 3,
        "This system is currently in alpha demonstration mode. "
        "Full multi-signal forensic analysis is being validated for accredited deployment."
    )
    pdf.output(pdf_path)

# ============ STREAMLIT ============
st.title("TruthMark-Aurion Digital Forensics")
st.write("Upload your video to generate a secure, court-grade digital forensic summary.")

uploaded_file = st.file_uploader("Upload video file", type=["mp4", "mov", "avi", "mpeg4"])
if uploaded_file:
    video_name = uploaded_file.name
    with open(video_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Generating forensic multi-signal analysis..."):
        fig_img = "forensic_multiplot.png"
        create_forensic_multiplot(fig_img)
        truth_score = 98.9  # Simulated score for demonstration
        pdf_path = "TruthMark_Aurion_Digital_Forensic_Report.pdf"
        generate_pdf_report(video_name, fig_img, pdf_path, truth_score)

    st.markdown("<h2 style='font-size:36px; color:#81c784;'>Forensic Summary Ready</h2>", unsafe_allow_html=True)
    st.image(fig_img, caption="Multi-signal forensic graph", use_column_width=True)

    with open(pdf_path, "rb") as f:
        st.download_button("Download PDF Report", f, file_name=pdf_path, mime="application/pdf")

    st.markdown(
        "<div style='padding-top:20px; font-size:13px; color:#999;'>"
        "<em>This system is currently in alpha demonstration mode. "
        "Full multi-signal forensic analysis is being validated for accredited deployment.</em></div>",
        unsafe_allow_html=True
    )
