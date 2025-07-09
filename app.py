# ===== INTAKE LAB NODE =====
st.markdown("""
    <style>
        .upload-block {
            background-color: #111;
            border: 1px solid #444;
            padding: 25px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .upload-title {
            font-size: 28px;
            color: #00e6b8;
            text-align: center;
            font-family: 'Courier New';
        }
        .pulse-bar {
            width: 100%;
            height: 12px;
            background: linear-gradient(to right, #00e6b8 0%, #003b35 50%, #00e6b8 100%);
            animation: pulse 1.8s infinite linear;
            border-radius: 5px;
            margin-top: 20px;
        }
        @keyframes pulse {
            0% { background-position: 0% }
            100% { background-position: 200% }
        }
    </style>
    <div class="upload-block">
        <h2 class="upload-title">🧾 Uplink Subject Footage</h2>
        <p style='text-align: center; color:#aaa'>Formats accepted: .mp4 | .mov | .avi</p>
    </div>
""", unsafe_allow_html=True)

video_file = st.file_uploader("", type=["mp4", "mov", "avi"])

if video_file and not st.session_state.analysis_complete:
    st.markdown("<div class='pulse-bar'></div>", unsafe_allow_html=True)
    st.info("Initializing biometric-linguistic signal calibration...")
    
    progress = st.empty()
    for i in range(100):
        time.sleep(0.012)
        progress.progress(i + 1)

    st.session_state.analysis_complete = True
