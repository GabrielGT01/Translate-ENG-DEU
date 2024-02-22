import streamlit as st
from transformers import pipeline

st.cache()

model = pipeline('translation',model = 'Helsinki-NLP/opus-mt-en-de')

def main():
    st.title("Translate short English text to German")
    st.subheader("Powered by hugging face transformers created by Gabriel")

    # Create an input text box
    input_text = st.text_input("Enter your text", "")

    # Create a button to trigger model inference
    if st.button("Translate"):
        # Perform inference using the loaded model
        result = model(input_text)
    
        st.write("Translated text :", result[0]['translation_text'])

if __name__ == "__main__":
    main()