import streamlit as st

#1 Define the dictionary data
nigeria_dict = {
    "igbo": {
        "ndewo": "hello",
             "mmiri": "water",
             "nri": "food",
             "ulo": "house",
        "oru": "work"

    },
    "yoruba":{
        "bawo": "hello",
              "ese": "thank you",
              "beeni": "yes",
              "ounje": "food",
        "ife": "house"
    },

    "igala":{
        "olodudu": "good ,morning",
             "oroka": "good afternoon",
             "ulane": "good evening",
             "aja": "market",
             "unyi": "house"
    },

    "hausa":{
        "dan allah": "please",
             "eh": "yes",
             "kudi": "money",
             "rana": "day",
             "namiji": "man",
    },

    "akan":{
        "nwoma": "book",
            "odo": "love",
            "abofra": "child",
            "anadwo": "night",
            "sukuu": "school",
    }
}

#2. streamlit UI Layout
st.title("NG Mini Nigerian Language Dictionary")
st.write("Select a Language and a word to see its English meaning.")

st.set_page_config(page_title="Don-pedro dictionary", page_icon="NG")

# Language Selection
language = st.selectbox("Choose a Language", list(nigerian_dict.keys()))

# Word Selection based on chosen language
if language:
    words = list(nigerian_dict[language].keys())
    selected_word = st.selectbox(f"Select a {language} words", words)

    # Display the Result
    meaning = nigerian_dict[language][selected_word]
    st.success(f"The English meaning of '**{selected_word}**' is: **{meaning}**")

# sidebar info
st.sidebar.header("About")
st.sidebar.info("This app features 5 major Nigerian languages: Igbo, Yoruba, Hausa, Igala, and Akan .")