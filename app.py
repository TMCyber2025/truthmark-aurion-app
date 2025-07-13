# 🧠 Validation Result Display
result = run_demo(base_path, subject_path, "", "")

verdict = result.get("verdict", "Undetermined")
confidence = result.get("confidence", "N/A")
anomalies = result.get("anomalies", [])
baseline_hash = result.get("baseline_hash", "")
subject_hash = result.get("subject_hash", "")

st.subheader("🧠 Validation Outcome")

# Verdict & Confidence Metric
st.markdown(f"### Verdict: **{verdict}**")
st.metric(label="Confidence Score", value=confidence)

# Verdict Status Message
if verdict.lower() == "truth":
    st.success("✅ Evidence aligns with baseline. No discrepancies found.")
elif verdict.lower() == "deception":
    st.error("🚨 Integrity breach detected. Evidence does not match baseline.")
else:
    st.warning("⚠️ Verdict undetermined. Further analysis recommended.")

# Hash Summaries
st.markdown("#### 🔐 Evidence Fingerprints")
st.code(f"Baseline Hash: {baseline_hash}\nSubject Hash: {subject_hash}", language="text")

# Anomalies List
st.markdown("#### 🔍 Anomaly Flags")
if anomalies:
    for item in anomalies:
        st.write(f"- {item}")
else:
    st.write("No anomalies detected.")

# Optional: Confidence Progress Bar (based on float conversion)
try:
    percent = float(confidence.strip("%")) / 100
    st.progress(percent)
except:
    pass  # Skip if confidence is not numeric

# Optional: Video Previews
with st.expander("🎞️ Preview Uploaded Videos"):
    st.video(base_path, format="video/mp4")
    st.video(subject_path, format="video/mp4")
