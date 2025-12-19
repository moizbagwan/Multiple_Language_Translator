import streamlit as st
import base64
from pathlib import Path

# ---------- Helper: Background Image ----------
def set_background(image_file: str):
    img_path = Path(image_file)
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
        background: rgba(255, 255, 255, 0.88);
        padding: 2rem;
        border-radius: 1.5rem;
        box-shadow: 0 18px 40px rgba(0,0,0,0.35);
        backdrop-filter: blur(8px);
    }}
    .big-title {{
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 4px 15px rgba(0,0,0,0.6);
    }}
    .sub-title {{
        font-size: 1.2rem;
        color: #f0f0f0;
        text-shadow: 0 2px 8px rgba(0,0,0,0.5);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# ---------- Home Page ----------
def main():
    st.set_page_config(
        page_title="Multi Language Translator",
        page_icon="🌍",
        layout="wide"
    )

    # Background image set 
    set_background("bg.jpg")

    # Sidebar content
    st.sidebar.title("🌍 Multi Language Translator")
    st.sidebar.markdown(
        """
        **Pages:**
        - Home  
        - Translator  
        - About / Help  
        """
    )
    st.sidebar.markdown("---")
    st.sidebar.info("Tip: Go to **Translator** page from left sidebar menu.")

    # Main content
    st.markdown("<div class='big-title'>Multi Language Translator</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Translate text into multiple languages with voice output, all in one beautiful app.</div>", unsafe_allow_html=True)
    st.write("")
    st.write("")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### ✨ What this app can do")
        st.markdown(
            """
            - 🔁 Translate any text into multiple languages  
            - 🎧 Listen to the translated text as **audio (Text-to-Speech)**  
            - ⬇ Download the generated audio file (MP3)  
            - 🖼 Enjoy a clean, modern UI with a background image  
            """
        )
        st.markdown("### 🚀 How to start")
        st.markdown(
            """
            1. Go to **Translator** page from the sidebar  
            2. Type your text  
            3. Select target language  
            4. Get translation + audio  
            """
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("### 💡 Tech used")
        st.markdown(
            """
            - `Streamlit` for UI  
            - `mtranslate` for translation  
            - `gTTS` for text-to-speech  
            - `pandas` for language CSV  
            """
        )
        st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
