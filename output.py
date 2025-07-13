# output.py

import streamlit as st

def display_verdict(verdict, confidence):
    st.subheader("🧠 Validation Outcome")
    st.markdown(f"### Verdict: **{verdict}**")
    st.metric(label="Confidence Score", value=confidence)

    if verdict.lower() == "truthful":
        st.success("✅ Evidence aligns with baseline. No discrepancies detected.")
    elif verdict.lower() == "deception":
        st.error("🚨 Integrity breach detected. Evidence does not match baseline.")
    else:
        st.warning("⚠️ Verdict unclear. Further analysis recommended.")

def display_hashes(baseline_hash, subject_hash):
    st.markdown("#### 🔐 Evidence Fingerprints")
    st.code(f"Baseline Hash: {baseline_hash}\nSubject Hash: {subject_hash}", language="text")

def display_anomalies(anomalies):
    st.markdown("#### 🔍 Anomaly Flags")
    if anomalies:
        for item in anomalies:
            st.write(f"- {item}")
    else:
        st.write("No anomalies detected.")

def display_progress(confidence):
    try:
        percent = float(confidence.strip("%")) / 100
        st.progress(percent)
    except:
        pass

def preview_videos(baseline_path, subject_path):
    with st.expander("🎬 Preview Videos"):
        st.video(baseline_path)
        st.video(subject_path)
