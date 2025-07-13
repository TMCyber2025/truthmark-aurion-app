import streamlit as st

# ================
# Page Config
# ================
st.set_page_config(page_title="TruthMark-Aurion — Investor Deck", layout="wide")

# ================
# Hero Section
# ================
st.markdown("""
<div style="text-align: center; padding: 3rem;">
    <h1 style="color: #7ec8ff; font-size: 3.5rem; font-family: monospace;">
        TruthMark-Aurion
    </h1>
    <h3 style="color: #cfd8e3; font-weight: 300; font-family: monospace;">
        Guardian of the Truth
    </h3>
    <p style="color: #a8b5c3; font-size: 1.2rem; max-width: 800px; margin: auto;">
        Revolutionising forensic truth detection with 333+ live biometric sensors,
        real-time SHA-256 chain of custody, and courtroom-grade analysis.
    </p>
</div>
""", unsafe_allow_html=True)

# ================
# Problem & Solution
# ================
st.markdown("""
<div style="background-color: #0e1a2e; padding: 2rem; border-radius: 10px; margin: 2rem;">
<h2 style="color: #7ec8ff; font-family: monospace;">The Problem</h2>
<p style="color: #cfd8e3; font-size: 1.1rem;">
Traditional polygraphs and so-called AI lie detectors are outdated, error-prone, and legally fragile.
They miss micro-behaviors, voice inconsistencies, and lack secure audit trails — leaving courts, businesses, and families exposed.
</p>

<h2 style="color: #7ec8ff; font-family: monospace;">Our Solution</h2>
<p style="color: #cfd8e3; font-size: 1.1rem;">
TruthMark-Aurion fuses video, audio, and biometric data across 333+ forensic modules, generating a secure, 
timestamped, cryptographically hashed report with unparalleled accuracy — designed for serious legal scrutiny.
</p>
</div>
""", unsafe_allow_html=True)

# ================
# Features
# ================
st.markdown("""
<div style="padding: 2rem;">
<h2 style="color: #7ec8ff; font-family: monospace;">Key Capabilities</h2>
<ul style="color: #cfd8e3; font-size: 1.1rem;">
    <li>✅ Multi-channel biometric truth verification</li>
    <li>✅ Secure SHA-256 chain-of-custody</li>
    <li>✅ Court-admissible PDF verdicts</li>
    <li>✅ Real-time emotion & micro-expression tracking</li>
    <li>✅ AI-driven truth vs deception scoring</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ================
# Demo Verdict
# ================
st.markdown("""
<div style="background-color: #152f44; padding: 2rem; border-radius: 10px; margin: 2rem;">
<h3 style="color: #7ec8ff; font-family: monospace;">Demo Forensic Verdict</h3>
<pre style="color: #cfd8e3; font-family: monospace; font-size: 1rem;">
✓ Chain of Custody: VERIFIED
✓ Biometric Match: 98.6% Confidence
✓ Timestamp Drift: ±0.02s
✓ SHA-256 Integrity: MATCHED

✅ VERDICT: AUTHENTIC — No Manipulative Artifacts Detected
</pre>
</div>
""", unsafe_allow_html=True)

# ================
# Founder Story & CTA
# ================
st.markdown("""
<div style="padding: 2rem;">
<h2 style="color: #7ec8ff; font-family: monospace;">Founder’s Mission</h2>
<p style="color: #cfd8e3; font-size: 1.1rem; max-width: 900px;">
Built from lived experience confronting false accusations and flawed systems, 
TruthMark-Aurion is my commitment to building a world where the truth stands above manipulation. 
Every line of code is written with that conviction.
</p>
<h4 style="color: #cfd8e3; font-family: monospace; margin-top:2rem;">
📧 Contact: sebbyisaac83@icloud.com
</h4>
</div>
""", unsafe_allow_html=True)

# ================
# Footer
# ================
st.markdown("<hr style='border:1px solid #294460;'>", unsafe_allow_html=True)
st.caption("© 2025 TruthMark-Aurion — Guardian of the Truth")
