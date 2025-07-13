# 🔧 Custom Forensic Background Styling
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://yourdomain.com/assets/bg-forensic-circuit.png");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
            background-color: #0a1d2b; /* Fallback forensic blue */
            color: white;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            background-color: rgba(10, 29, 43, 0.85);
            border-radius: 10px;
        }
        h1, h2, h3 {
            color: #f0f4f8;
            font-family: 'Orbitron', sans-serif;
        }
        .metric-label, .metric-value {
            font-family: 'Exo', sans-serif;
        }
        .stButton>button {
            background-color: #1976d2;
            color: white;
            border-radius: 6px;
        }
    </style>
""", unsafe_allow_html=True)
