import streamlit as st
from deep_translator import GoogleTranslator

def translate(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

# Streamlit app
st.title("Language Translator")

# Input text from the user
text = st.text_area("Enter text in any language:")

# Button to trigger translation
if st.button("Translate"):
    if text:
        translated_text = translate(text)
        st.success(f"Translated Text: {translated_text}")
    else:
        st.error("Please enter some text to translate.")
