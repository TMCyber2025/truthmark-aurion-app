# 🔧 Forensic Landing Page Styling
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://yourdomain.com/assets/bg-forensic-circuit-lightblue.png");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
            background-color: #0e2a45; /* Fallback forensic blue */
        }

        .block-container {
            padding-top: 4rem;
            padding-bottom: 4rem;
            background-color: rgba(14, 42, 69, 0.85); /* Semi-transparent overlay */
            border-radius: 12px;
        }

        h1, h2, h3 {
            color: #f0f4f8;
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 0.8px;
        }

        p, label, .markdown-text-container {
            color: #cfd8e3;
            font-family: 'Exo', sans-serif;
        }

        .stButton>button {
            background-color: #1976d2;
            color: white;
            font-weight: 600;
            border-radius: 6px;
            padding: 0.6rem 1.2rem;
        }

        .stMetric {
            background-color: rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            padding: 0.5rem;
        }

        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)
