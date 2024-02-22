import streamlit as st
from transformers import pipeline

st.cache()

eng= pipeline('translation',model = 'Helsinki-NLP/opus-mt-en-de')
deu= pipeline('translation',model = 'Helsinki-NLP/opus-mt-de-en')

def main():
    st.title("Translation for short text to German")
    st.subheader("Powered by  transformers created by Gabriel")

    Languages = ["German to English", "English to German"]

    choice = st.sidebar.selectbox("Language", Languages)

    if choice == "English to German":
        # Create an input text box
        input_text = st.text_input("Enter your text", "")

        # Create a button to trigger model inference
        if st.button("Translate"):

        # Perform inference using the loaded model
           result = eng-deu(input_text)
           st.write("Translated text :", result[0]['translation_text'])



    else:
        input_text = st.text_input("Enter your text", "")

        # Create a button to trigger model inference
        if st.button("Translate"):

        # Perform inference using the loaded model
           result = deu-eng(input_text)
           st.write("Translated text :", result[0]['translation_text'])




if __name__ == "__main__":
    main()