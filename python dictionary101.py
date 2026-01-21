import streamlit as st

yoruba_dictionary = {
    "hello": "bawo",
    "food": "ounje",
    "water": "omi",
    "house": "ile"
}

st.title("English to Yoruba Dictionary")

language = st.selectbox("Choose a language", ["yoruba"])
word = st.text_input("Enter an English word")

if word:
    if word.lower() in yoruba_dictionary:
        st.success(f"Translation: {yoruba_dictionary[word.lower()]}")
    else:
        st.error("Word not found")







                       


