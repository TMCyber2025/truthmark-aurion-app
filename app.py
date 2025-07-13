# 🚀 Run Validation
if st.button("Run Forensic Validation"):
    st.markdown("### 📽️ Processing Videos... Please wait.")
    with st.spinner("Running integrity analysis..."):

        # ✅ Step 1: Validate Baseline Upload
        if baseline_video is not None:
            base_path = save_file(baseline_video, "data/baseline.mp4")
        else:
            st.error("❌ Baseline video is missing. Please upload known truthful content.")
            st.stop()

        # ✅ Step 2: Validate Subject Input
        if use_webcam and os.path.exists("uploads/webcam_input.mp4"):
            subject_path = "uploads/webcam_input.mp4"
            st.info("Using webcam input as subject video.")
        elif subject_video is not None:
            subject_path = save_file(subject_video, "data/subject.mp4")
        else:
            st.error("❌ Subject video is missing. Upload or record subject input.")
            st.stop()

        # ✅ Step 3: Run Forensic Validation
        result = run_demo(base_path, subject_path, "", "")

        # ✅ Step 4: Display Results
        verdict = result.get("verdict", "Undetermined")
        confidence = result.get("confidence", "N/A")
        anomalies = result.get("anomalies", [])
        baseline_hash = result.get("baseline_hash", "")
        subject_hash = result.get("subject_hash", "")

        st.subheader("🧠 Validation Outcome")
        st.markdown(f"### Verdict: **{verdict}**")
        st.metric(label="Confidence Score", value=confidence)

        # 🟢 Verdict Status
        if verdict.lower() == "truthful":
            st.success("✅ Evidence aligns with baseline. No discrepancies found.")
        elif verdict.lower() == "deception":
            st.error("🚨 Integrity breach detected. Evidence does not match baseline.")
        else:
            st.warning("⚠️ Verdict undetermined. Further analysis recommended.")

        # 🔐 Hash Summary
        st.markdown("#### 🔐 Evidence Fingerprints")
        st.code(f"Baseline Hash: {baseline_hash}\nSubject Hash: {subject_hash}", language="text")

        # 🔍 Anomaly Breakdown
        st.markdown("#### 🔍 Anomaly Flags")
        if anomalies:
            for item in anomalies:
                st.write(f"- {item}")
        else:
            st.write("No anomalies detected.")

        # 📊 Confidence Progress Bar (if valid number)
        try:
            percent = float(confidence.strip("%")) / 100
            st.progress(percent)
        except:
            pass

        # 🎞️ Video Previews
        with st.expander("🎬 Preview Videos"):
            st.video(base_path, format="video/mp4")
            st.video(subject_path, format="video/mp4")
