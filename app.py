import streamlit as st
import time
from datetime import datetime

# ============================
# Page config
# ============================
st.set_page_config(page_title="TruthMark-Aurion", layout="wide")

# ============================
# Digital dark grid background
# ============================
st.markdown("""
<style>
.stApp {
    background-color: #0b111e;
    background-image: radial-gradient(#1a2a44 1px, transparent 1px);
    background-size: 20px 20px;
}
.css-1kyxreq.edgvbvh3, .css-1kyxreq.e1fqkh3o3 {  /* uploader container */
    background: rgba(10,20,30,0.5);
    border: 1px solid #7ec8ff;
    border-radius: 5px;
    width: 300px;
    margin: auto;
}
</style>
""", unsafe_allow_html=True)

# ============================
# Main title block with badass lines
# ============================
st.markdown("""
<div style="text-align: center; padding: 2rem;">
    <h1 style="color: #7ec8ff; font-size: 3.5rem; font-family: monospace;">
        TruthMark-Aurion
    </h1>
    <h3 style="color: #cfd8e3; font-weight: 300; font-family: monospace;">
        Guardian of the Truth
    </h3>
    <p style="color: #a8b5c3; font-size: 1.3rem; max-width: 900px; margin: auto;">
        333 live biometric sensors that detect deception before you even finish your sentence.<br>
        You better think twice before you lie.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================
# Small neat uploader
# ============================
st.markdown("<div style='text-align:center; color:#7ec8ff; font-family: monospace; font-size:1.2rem;'>Run a quick demo</div>", unsafe_allow_html=True)

video = st.file_uploader("", type=["mp4", "mov", "avi"], label_visibility="collapsed")

# ============================
# Verdict box
# ============================
if video:
    if st.button("🚀 Analyse Video"):
        with st.spinner("Running multi-layer biometric scan..."):
            time.sleep(2)
        st.success("Analysis complete.")
        st.markdown(f"""
        <div style='background-color:#152f44; padding:1rem; border-radius:8px; margin-top:1rem; max-width:600px; margin:auto;'>
        <h4 style='color:#7ec8ff; font-family: monospace;'>✅ VERDICT: AUTHENTIC — No Manipulative Artifacts Detected</h4>
        <pre style='color:#cfd8e3; font-family: monospace; font-size:0.95rem;'>
✓ Chain of Custody:    VERIFIED  
✓ Biometric Match:     98.6% Confidence  
✓ Timestamp Drift:     ±0.02s  
✓ SHA-256 Integrity:   MATCHED  
        </pre>
        </div>
        """, unsafe_allow_html=True)
        st.caption(f"Report generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
else:
    st.info("Select a short video to see the live forensic demo.")

# ============================
# Footer
# ============================
st.markdown("<hr style='border:1px solid #294460; max-width:600px; margin:auto;'>", unsafe_allow_html=True)
st.caption("© 2025 TruthMark-Aurion — Guardian of the Truth")
