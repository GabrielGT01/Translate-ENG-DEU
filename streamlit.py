import streamlit as st
from transformers import pipeline

st.cache()

model = pipeline('translation',model = 'Helsinki-NLP/opus-mt-en-de')

def main():
    st.title("Translation for short text to German")
    st.subheader("Powered by  transformers created by Gabriel")

    Languages = ["German to English", "English to German"]

    choice = st.sidebar.selectbox("Language", Languages)
    if choice == "German to English":
        # Create an input text box
        input_text = st.text_input("Enter your text", "")

        # Create a button to trigger model inference
        if st.button("Translate"):
        # Perform inference using the loaded model
        result = model(input_text)
    
        st.write("Translated text :", result[0]['translation_text'])



    else:
        

if __name__ == "__main__":
    main()