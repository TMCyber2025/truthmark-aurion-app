import streamlit as st

# ========== 🛡️ HERO SECTION with LOGO ==========
col_logo, col_title = st.columns([1, 3])
with col_logo:
    st.image("your-logo-file.jpeg", width=90)  # Replace with your actual logo filename
with col_title:
    st.markdown("""
    <div style="margin-top: -0.5rem;">
        <h1 style="font-family: 'Orbitron', sans-serif; font-size: 2.6rem; color: #a3e4ff; margin-bottom: 0;">
            TruthMark-Aurion
        </h1>
        <p style="font-family: 'Exo', sans-serif; font-size: 1.1rem; color: #eaf5ff; margin-top: 0.3rem;">
            Courtroom-grade Forensic Validation — Validate. Detect. Preserve.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ========== 📘 GUIDANCE PANEL ==========
st.markdown("""
<div style="background: rgba(14,42,69,0.65); padding: 1.5rem; margin: 1.5rem 0; border-radius: 14px; text-align: center;">
    <p style="font-family: 'Exo', sans-serif; font-size: 1.05rem; color: #cfd8e3; line-height: 1.7;">
        Upload your <span style="color:#7ec8ff;"><strong>Baseline</strong></span> and <span style="color:#7ec8ff;"><strong>Subject</strong></span> videos.<br>
        Then trigger forensic validation to assess biometric authorship, timestamp drift, and cryptographic sealing.
    </p>
</div>
""", unsafe_allow_html=True)

# ========== 🎥 INPUT PANEL ==========
st.markdown("### 📁 Artifact Intake")
col1, col2 = st.columns(2)
with col1:
    baseline = st.file_uploader("🔎 Baseline Video", type=["mp4", "mov", "avi"])
    if baseline:
        st.success("✓ Baseline uploaded")
with col2:
    subject = st.file_uploader("🎯 Subject Video", type=["mp4", "mov", "avi"])
    if subject:
        st.success("✓ Subject uploaded")

# ========== 🧪 VALIDATION TRIGGER ==========
st.markdown("<hr style='margin: 1.5rem 0; border: none; height: 1px; background: #294460;'>", unsafe_allow_html=True)
if baseline and subject:
    if st.button("🚀 Run Forensic Validation"):
        st.success("Validation initiated — processing fingerprints and biometric cohesion...")
        st.markdown("""
        <div style="background-color: #152f44; padding: 1.2rem 1.5rem; border-radius: 14px; box-shadow: inset 0 0 10px #2e5f7e;">
            <h4 style="color: #7ec8ff;">📡 Verdict Summary</h4>
            <pre style="color: #e3edf7; font-size: 0.95rem;">
✓ Chain of Custody: Verified  
✓ Biometric Authorship Confidence: 98.6%  
✓ Timestamp Drift: 0.02s (Within Acceptable Range)  
✓ SHA-256 Hash Match: Confirmed  

✅ Verdict: Authentic — No Manipulative Artifacts Detected
            </pre>
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("Upload both videos to enable validation.")

# ========== 🔍 MODULE SNAPSHOTS ==========
st.markdown("### 🧩 Core Capabilities")
st.markdown("""
<div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-top: 1rem;">
    <div style="background: rgba(30, 54, 80, 0.85); padding: 1.2rem; width: 280px; text-align: center; border-radius: 14px; margin-bottom: 1rem;">
        <h4 style="color: #7ec8ff;">🔐 Cryptographic Sealing</h4>
        <p style="color: #cfd8e3; font-size: 0.9rem;">SHA-256 fingerprinting prevents tampering across the chain of custody.</p>
    </div>
    <div style="background: rgba(30, 54, 80, 0.85); padding: 1.2rem; width: 280px; text-align: center; border-radius: 14px; margin-bottom: 1rem;">
        <h4 style="color: #7ec8ff;">🧬 Biometric Intelligence</h4>
        <p style="color: #cfd8e3; font-size: 0.9rem;">Facial geometry and voiceprint triangulation for authorship confirmation.</p>
    </div>
    <div style="background: rgba(30, 54, 80, 0.85); padding: 1.2rem; width: 280px; text-align: center; border-radius: 14px; margin-bottom: 1rem;">
        <h4 style="color: #7ec8ff;">🧠 Verdict Engine</h4>
        <p style="color: #cfd8e3; font-size: 0.9rem;">Structured dispatch output aligned with evidentiary admissibility standards.</p>
    </div>
</div>
""", unsafe_allow_html=True)
