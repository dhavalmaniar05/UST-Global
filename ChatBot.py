import streamlit as st
import openai
from streamlit_chat import message
from dotenv import load_dotenv
import os

load_dotenv()
openai.organization = "org-2Mok0YRnTfHOVbx3EJXTXZOu"
openai.api_key = os.getenv("OPENAI_API_KEY")

if 'history' not in st.session_state:
    st.session_state['history'] = []
    st.session_state['history'].append({"message": "Hello", "is_user": False})


def Generate_Response():
    user_message = st.session_state.input_text

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Q:What is obsessive-compulsive personality disorder?\nA:Obsessive-compulsive personality disorder (OCPD) is a personality disorder that is characterized by a rigid adherence to rules and regulations, an obsession with details and orderliness, and a need for control. People with OCPD often have difficulty completing tasks and may be overly critical of others.\n\nQ: What is obsessive-compulsive personality disorder?\nA: Obsessive-compulsive personality disorder (OCPD) is a personality disorder that is characterized by a rigid adherence to rules and regulations, an obsession with details and orderliness, and a need for control. People with OCPD often have difficulty completing tasks and may be overly critical of others.\n\nQ:What is antisocial personality disorder? \nA:Antisocial personality disorder is a personality disorder characterized by a lack of empathy and a disregard for the rights of others. People with this disorder often engage in criminal behavior and may be manipulative or callous.\n\nQ: " + user_message + "\nA:",
        temperature=0.25,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.25,
        presence_penalty=0.15,
        stop=["\n"]
    )

    st.session_state['history'].append(
        {"message": user_message, "is_user": True})
    st.session_state['history'].append(
        {"message": response['choices'][0]['text'], "is_user": False})


st.text_input("You:", key="input_text", on_change=Generate_Response)

count = 0
for chat in reversed(st.session_state["history"]):
    message(**chat, key=count)
    count += 1
