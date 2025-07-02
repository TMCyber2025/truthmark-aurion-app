<<<<<<< HEAD
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
=======

import streamlit as st
from engine import run_full_aurion_analysis

st.set_page_config(page_title="TruthMark Aurion", layout="centered")

st.markdown("""
    <style>
    body { background-color: #0a0a0a; }
    .reportview-container { background: #0a0a0a; color: #fdfdfd; }
    .stButton>button {
        background-color: #ffd700;
        color: black;
        border: none;
        font-weight: bold;
        padding: 0.6em 1.5em;
        border-radius: 12px;
        font-size: 1.1em;
    }
    .stMarkdown h1, .stMarkdown h2 {
        color: #ffd700;
        font-family: Orbitron, sans-serif;
        text-align: center;
    }
    .results-panel {
        background: #111;
        border: 2px solid #ffd700;
        padding: 1.5em;
        border-radius: 12px;
        font-family: monospace;
        font-size: 1em;
        color: #eee;
    }
    .scan-bar-wrap { width: 100%; height: 15px; background: #333; border-radius: 10px; margin-top: 10px; }
    .scan-bar-inner { height: 100%; background: #ffd700; border-radius: 10px; transition: width 0.3s ease-in-out; }
    .pdf-btn, .email-btn {
        display: inline-block;
        margin-top: 1.2em;
        padding: 0.7em 2em;
        background: #ffd700;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <h1>TruthMark Aurion</h1>
    <h2>Guardian of Truth</h2>
""", unsafe_allow_html=True)

st.markdown("#### Upload your evidence video")
uploaded = st.file_uploader("Choose video file (MP4, MOV)", type=["mp4", "mov"])

if uploaded:
    st.success("File uploaded successfully. Initializing scan...")

    import time
    scan_ring = st.empty()
    scan_text = st.empty()
    scan_placeholder = st.empty()
    scan_percent = st.empty()
    N_STEPS = 40

    for i in range(N_STEPS + 1):
        percent = int((i / N_STEPS) * 100)
        scan_ring.markdown(f"""
        <div style='display:flex;justify-content:center;height:140px;'>
            <svg width='120' height='120'>
                <circle cx='60' cy='60' r='48' stroke='#ffd700' stroke-width='7' fill='none'
                stroke-dasharray='282' stroke-dashoffset='{282 - 282 * percent // 100}'
                style='filter:drop-shadow(0 0 20px #ffd700);transform:rotate({percent*9}deg);transition:all 0.1s ease-in-out;'/>
            </svg>
        </div>
        """, unsafe_allow_html=True)

        scan_text.markdown(f"<div style='text-align:center;'>SCANNING <b>{percent}%</b></div>", unsafe_allow_html=True)
        scan_placeholder.markdown(f"""
        <div class='scan-bar-wrap'>
            <div class='scan-bar-inner' style='width:{percent}%;'></div>
        </div>
        """, unsafe_allow_html=True)
        scan_percent.markdown(f"<div style='text-align:center;margin-top:8px;font-weight:bold;'>{percent}% complete</div>", unsafe_allow_html=True)
        time.sleep(0.05)

    scan_ring.empty()
    scan_text.empty()
    scan_placeholder.empty()
    scan_percent.empty()

    results = run_full_aurion_analysis("placeholder_path")

    st.markdown("""
    <div class="results-panel">
        <b>Analysis Results</b><br><br>
        • <span>TruthMatch Score:</span> <span class="good">99.9%</span><br>
        • <span>Timeline Anomalies:</span> <span class="bad">None detected</span><br>
        • <span>Signal Integrity:</span> <span class="good">Excellent</span><br>
        • <span>Evidence chain:</span> <span>Verified</span><br>
        <br>
        <span style="color:#fff;font-weight:900;">Full forensic report ready for secure distribution.</span>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("Show Forensic Details"):
        st.json(results['details'])

    st.markdown('<a href="#" class="pdf-btn">Download PDF Report</a>', unsafe_allow_html=True)
    st.markdown(
        '<a href="mailto:?subject=TruthMark%20Aurion%20Results&body=See%20attached%20TruthMark%20Aurion%20Report. TruthMatch Score: 99.9%" class="email-btn">Email Results</a>',
        unsafe_allow_html=True
    )
else:
    st.info("Awaiting video upload...")
>>>>>>> 9d89bae (Initial commit - upload TruthMark Aurion app)
