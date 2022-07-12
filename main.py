import streamlit as st
import openai
import os

st.title("Keyword Extraction using GPT-3")
input = st.text_area("Input the content whose keywords need to be extracted:")

openai.api_key = "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"
form = st.form("my_form")
# Now add a submit button to the form:
form.form_submit_button("submit")
input = 'Extract keywords from this text:\n\n' + input
response = openai.Completion.create(
  model="text-curie-001",
    prompt=input,
  temperature=0.8,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.8,
  presence_penalty=0.0)
st.text('Keywords:')
st.text(response["choices"][0]["text"])


# steps : OPEN TERMINAL AND WRITE ALL THIS:
# cd programming/python/ps1\(1\)
# source ./env/bin/activate
# streamlit run /Users/neha/programming/python/ps1\(1\)/main.py

