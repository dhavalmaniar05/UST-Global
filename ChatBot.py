import streamlit as st
import openai
from streamlit_chat import message

openai.organization = "Org_Key" #Use your Organization Key here
openai.api_key ="API_Key"  #Use your API-Key here

if "history" not in st.session_state:
    st.session_state['history'] = []
    st.session_state['history'].append({"message": "Hello", "is_user": False})

def Generate_Response():
    user_message = st.session_state.input_text

    response = openai.Completion.create(
        model = "text-davinci-002",            
        prompt = "I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: " + user_message + "\nA:",
        temperature = 0.0,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0,
        stop=["\n"] 
        )

    st.session_state['history'].append({"message": user_message, "is_user": True})
    st.session_state['history'].append({"message": response['choices'][0]['text'], "is_user": False})

st.text_input("You:", key = "input_text", on_change = Generate_Response)

count = 0
for chat in reversed(st.session_state["history"]):
    message(**chat, key = count)
    count += 1