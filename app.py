import streamlit as st
import cv2
import tempfile
import time
import numpy as np
from fpdf import FPDF
from datetime import datetime
import matplotlib.pyplot as plt

# =============== PAGE CONFIG & BACKGROUND WATERMARK ==============
st.set_page_config(page_title="TruthMark-Aurion", page_icon=":shield:", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background: url("https://raw.githubusercontent.com/TMCyber2025/truthmark-aurion-app/main/lady_justice.jpg") no-repeat center center fixed;
        background-size: 50%;
        filter: invert(1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =============== HEADER & LOGO ==============
st.markdown("<h1 style='text-align: center; color: #00FFAA;'>TruthMark-Aurion</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Guardian of the Truth</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #AAAAAA;'>Quantum Overseer</h4>", unsafe_allow_html=True)
st.markdown("---")

# =============== INPUT CHOICE: UPLOAD OR WEBCAM ==============
option = st.radio("Select input method:", ("Upload Video", "Use Webcam"))

video_file = None

if option == "Upload Video":
    video_file = st.file_uploader("Upload a video file", ty
