import streamlit as st
import base64
from pathlib import Path

def set_background(image_file: str):
    img_path = Path(__file__).resolve().parents[1] / image_file
    if not img_path.exists():
        return

    with open(img_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    css = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/jpeg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    [data-testid="stSidebar"] {{
        background: rgba(0, 0, 0, 0.55);
        color: white;
    }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
    }}
    .glass-card {{
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 1.5rem;
        box-shadow: 0 16px 35px rgba(0,0,0,0.3);
        backdrop-filter: blur(8px);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="About",
        page_icon="ℹ️",
        layout="centered"
    )

    set_background("bg.jpg")

    st.markdown("<h2 style='color:white;text-shadow:0 3px 8px rgba(0,0,0,0.6);'>ℹ️ About this App</h2>", unsafe_allow_html=True)
    st.write("")

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown(
        """
        ### 🎯 Purpose  
        This application is built to make language translation and learning easier and more interactive.  
        
        ### 🧩 Features
        - Multi-language text translation  
        - Text-to-speech audio generation  
        - Downloadable MP3 file  
        - Beautiful glassmorphism UI with background image  

        ### 🛠 Tech Stack
        - **Python**
        - **Streamlit**
        - **mtranslate**
        - **gTTS**
        - **pandas**

        ### 👨‍💻 Developer
        - Built by: **Abdul Moiz**  
        - Perfect project to showcase on **GitHub** and **LinkedIn** as:
          - *“Multi-language Text & Speech Translator using Streamlit”*
        """
    )
    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
