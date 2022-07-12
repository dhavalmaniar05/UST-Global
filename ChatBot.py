import openai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    st.title("ChatBot")
    Sentence = st.text_input("Human :")

    response = openai.Completion.create(
        model="ada:ft-bits-pilani-hyderabad-campus-2022-07-07-06-19-32",
        prompt="\n\nQ: " + Sentence + "\nA:",
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )

    if(Sentence == ""):
        st.text_area("Bot:", value="", height=200, max_chars=None, key=None)
    else:
        st.text_area("Bot:", value=response['choices'][0]
                     ['text'], height=200, max_chars=None, key=None)


main()
