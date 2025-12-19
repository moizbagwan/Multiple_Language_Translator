import streamlit as st
from mtranslate import translate
import pandas as pd
import os
from gtts import gTTS
import base64
from pathlib import Path

# ---------- Helper: Background Image + Styling (same as home) ----------
def set_background(image_file: str):
    img_path = Path(__file__).resolve().parents[1] / image_file  # go one level up
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
        padding: 1.8rem;
        border-radius: 1.5rem;
        box-shadow: 0 16px 35px rgba(0,0,0,0.3);
        backdrop-filter: blur(8px);
    }}
    .page-title {{
        font-size: 2rem;
        font-weight: 800;
        color: #ffffff;
        text-shadow: 0 4px 15px rgba(0,0,0,0.6);
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ---------- File downloader (same as your function, just reused) ----------
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href


def main():
    st.set_page_config(
        page_title="Translator",
        page_icon="🔁",
        layout="wide"
    )

    # Background
    set_background("bg.jpg")

    st.markdown("<div class='page-title'>🔁 Translator</div>", unsafe_allow_html=True)
    st.write("")

    # ---------- Load language data ----------
    # language.csv expected in project root (one level up from pages)
    csv_path = Path(__file__).resolve().parents[1] / "language.csv"
    if not csv_path.exists():
        st.error("❌ language.csv file not found. Please keep language.csv in the main project folder.")
        return

    df = pd.read_csv(csv_path)
    df.dropna(inplace=True)

    lang_names = df['name'].to_list()
    lang_codes = df['iso'].to_list()
    lang_array = {lang_names[i]: lang_codes[i] for i in range(len(lang_codes))}

    # gTTS supported languages (same as before)
    speech_langs = {
        "af": "Afrikaans",
        "ar": "Arabic",
        "bg": "Bulgarian",
        "bn": "Bengali",
        "bs": "Bosnian",
        "ca": "Catalan",
        "cs": "Czech",
        "cy": "Welsh",
        "da": "Danish",
        "de": "German",
        "el": "Greek",
        "en": "English",
        "eo": "Esperanto",
        "es": "Spanish",
        "et": "Estonian",
        "fi": "Finnish",
        "fr": "French",
        "gu": "Gujarati",
        "od": "odia",
        "hi": "Hindi",
        "hr": "Croatian",
        "hu": "Hungarian",
        "hy": "Armenian",
        "id": "Indonesian",
        "is": "Icelandic",
        "it": "Italian",
        "ja": "Japanese",
        "jw": "Javanese",
        "km": "Khmer",
        "kn": "Kannada",
        "ko": "Korean",
        "la": "Latin",
        "lv": "Latvian",
        "mk": "Macedonian",
        "ml": "Malayalam",
        "mr": "Marathi",
        "my": "Myanmar (Burmese)",
        "ne": "Nepali",
        "nl": "Dutch",
        "no": "Norwegian",
        "pl": "Polish",
        "pt": "Portuguese",
        "ro": "Romanian",
        "ru": "Russian",
        "si": "Sinhala",
        "sk": "Slovak",
        "sq": "Albanian",
        "sr": "Serbian",
        "su": "Sundanese",
        "sv": "Swedish",
        "sw": "Swahili",
        "ta": "Tamil",
        "te": "Telugu",
        "th": "Thai",
        "tl": "Filipino",
        "tr": "Turkish",
        "uk": "Ukrainian",
        "ur": "Urdu",
        "vi": "Vietnamese",
        "zh-CN": "Chinese"
    }

    # ---------- UI Layout ----------
    c_main, c_side = st.columns([3, 2])

    with c_main:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("📝 Enter text to translate")
        inputtext = st.text_area(
            "Type or paste your text here",
            height=150,
            placeholder="E.g. Hello, how are you?"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with c_side:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("🎯 Select target language")
        choice = st.selectbox("Language", options=lang_names)
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    c1, c2 = st.columns([3, 2])

    # ---------- Translation + Audio ----------
    if inputtext.strip():
        try:
            output = translate(inputtext, lang_array[choice])

            with c1:
                st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                st.subheader("✅ Translated Text")
                st.text_area("Result", output, height=200)
                st.markdown("</div>", unsafe_allow_html=True)

            # Check if language code supported by gTTS
            lang_code = lang_array[choice]
            if lang_code in speech_langs.keys():
                with c2:
                    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                    st.subheader("🎧 Listen / Download Audio")
                    aud_file = gTTS(text=output, lang=lang_code, slow=False)
                    file_name = "translated_audio.mp3"
                    aud_file.save(file_name)

                    with open(file_name, "rb") as f:
                        audio_bytes = f.read()

                    st.audio(audio_bytes, format="audio/mp3")
                    st.markdown(
                        get_binary_file_downloader_html(file_name, 'Audio File'),
                        unsafe_allow_html=True
                    )
                    st.markdown("</div>", unsafe_allow_html=True)
            else:
                with c2:
                    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                    st.warning("⚠ Audio not available for this language.")
                    st.markdown("</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Something went wrong: {e}")


if __name__ == "__main__":
    main()
