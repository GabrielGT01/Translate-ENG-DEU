import streamlit as st
from transformers import pipeline

st.cache()

#eng= pipeline('translation',model = 'Helsinki-NLP/opus-mt-en-de')
#3deu= pipeline('translation',model = 'Helsinki-NLP/opus-mt-de-en')

def main():
    st.title("Translation ")
    st.subheader("Powered by  transformers created by Gabriel")

    Languages = ["English 🇬🇧 to German  🇩🇪 "German 🇩🇪 to English 🇬🇧"]



    choice = st.selectbox("Language Option", Languages)

    if choice == "English to German":
        st.subheader(" English to German")
        # Create an input text box
        input_text = st.text_input("Enter your text", "")

        # Create a button to trigger model inference
        if st.button("Translate"):

        # Perform inference using the loaded model
           eng= pipeline('translation',model = 'Helsinki-NLP/opus-mt-en-de')
           result = eng(input_text)
           st.write("Translated text :", result[0]['translation_text'])



    else:


        st.subheader("Translating from German to English")
        input_text = st.text_input("Enter your text", "")

        # Create a button to trigger model inference
        if st.button("Translate"):
            # Perform inference using the loaded model
            deu= pipeline('translation',model = 'Helsinki-NLP/opus-mt-de-en')
            result = deu(input_text)
            st.write("Translated text :", result[0]['translation_text'])




if __name__ == "__main__":
    main()