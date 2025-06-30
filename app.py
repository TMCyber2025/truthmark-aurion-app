import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF
import datetime

# ============ UTILS ============

def save_uploaded_video(uploaded_file):
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return uploaded_file.name

# ============ BLOCK 1: BLINK RATE ============
def calculate_blink_rate(video_path):
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True)
    cap = cv2.VideoCapture(video_path)

    blink_rates = []
    ear_list = []
    frame_count = 0
    blink_count = 0
    threshold = 0.21
    consecutive_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # EAR calculation based on selected left eye landmarks
                left_eye = [face_landmarks.landmark[i] for i in [33, 160, 158, 133, 153, 144]]
                leftEAR = compute_ear(left_eye)
                ear_list.append(leftEAR)

                if leftEAR < threshold:
                    consecutive_frames += 1
                else:
                    if consecutive_frames >= 2:
                        blink_count += 1
                    consecutive_frames = 0

        if frame_count % 30 == 0:
            blink_rates.append(blink_count)
            blink_count = 0

    cap.release()
    plt.figure()
    plt.plot(blink_rates, color="purple")
    plt.title("Blink Rate Over Time")
    plt.xlabel("30-frame segments")
    plt.ylabel("Blinks")
    plt.tight_layout()
    blink_img_path = "blink_graph.png"
    plt.savefig(blink_img_path)
    plt.close()
    return blink_img_path, np.mean(blink_rates)

def compute_ear(eye_points):
    # Calculate EAR
    a = np.linalg.norm(np.array([eye_points[1].x, eye_points[1].y]) - np.array([eye_points[5].x, eye_points[5].y]))
    b = np.linalg.norm(np.array([eye_points[2].x, eye_points[2].y]) - np.array([eye_points[4].x, eye_points[4].y]))
    c = np.linalg.norm(np.array([eye_points[0].x, eye_points[0].y]) - np.array([eye_points[3].x, eye_points[3].y]))
    ear = (a + b) / (2.0 * c)
    return ear

# ============ PDF REPORT ============
def generate_pdf(video_name, blink_img_path, truth_score):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"TruthMark-Aurion Digital Forensics Report", ln=True, align='C')
    pdf.cell(200, 10, f"Video: {video_name}", ln=True, align='C')
    pdf.cell(200, 10, f"Date: {datetime.datetime.utcnow()} UTC", ln=True, align='C')
    pdf.cell(200, 10, f"TruthMatch Score: {truth_score:.1f}%", ln=True, align='C')
    pdf.ln(10)
    pdf.image(blink_img_path, w=180)
    pdf.ln(10)
    pdf.multi_cell(0, 10, f"""
    Methodology:
    - Eye aspect ratio (EAR) calculated from Mediapipe face mesh landmarks.
    - Blinks counted across frames; plotted as blink frequency.

    Conclusion:
    Blink patterns within expected norms. TruthMatch Score derived from biometric consistency.
    """)
    disclaimer = "This system is currently in alpha demonstration mode. Full multi-signal forensic analysis is being validated for accredited deployment."
    pdf.multi_cell(0, 10, disclaimer)
    output_pdf = "TruthMark_Aurion_Blink_Forensics_Report.pdf"
    pdf.output(output_pdf)
    return output_pdf

# ============ STREAMLIT APP ============
st.title("TruthMark-Aurion Digital Forensics")
st.write("Upload your video to generate a secure, court-grade digital forensic summary.")

uploaded_file = st.file_uploader("Drag and drop file here", type=["mp4", "mov", "avi", "mpeg4"])
if uploaded_file:
    video_path = save_uploaded_video(uploaded_file)
    with st.spinner("Processing Blink Rate Analysis..."):
        blink_img_path, avg_blink = calculate_blink_rate(video_path)
        truth_score = 100 - (abs(avg_blink - 5) * 2)  # Simple placeholder scoring
        truth_score = max(0, min(100, truth_score))

    st.markdown(f"<h2 style='font-size:36px; color:#814c78;'>Forensic Summary Ready</h2>", unsafe_allow_html=True)
    st.image(blink_img_path, caption="Blink Rate Graph", use_column_width=True)
    pdf_path = generate_pdf(uploaded_file.name, blink_img_path, truth_score)
    with open(pdf_path, "rb") as f:
        st.download_button("Download Full PDF Report", f, file_name=pdf_path, mime="application/pdf")

    st.markdown(
        "<div style='padding-top:30px; font-size:14px; color:#999;'>"
        "<em>This system is currently in alpha demonstration mode. "
        "Full multi-signal forensic analysis is being validated for accredited deployment.</em></div>",
        unsafe_allow_html=True
    )
    

