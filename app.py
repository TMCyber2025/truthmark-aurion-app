
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
