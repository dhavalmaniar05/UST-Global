import streamlit as st
import openai
import os

st.title("Keyword Extraction using GPT-3")
input = st.text_area("Input the content whose keywords need to be extracted:")

openai.api_key = "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"  # entering the API key to access GPT-3 model from OpenAI
form = st.form("my_form")                                               # inserting an input box for the user to enter his input
form.form_submit_button("submit")                                       # adding a submit button
input = 'Extract keywords from this text:\n\n' + input                  # invoking gpt-3 and telling it to extract keywords from the given input
response = openai.Completion.create(
  model="text-davinci-002",
    prompt=input,
  temperature=1,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=1.0,
  presence_penalty=1.0)                                                  # setting the parameters for the gpt-3 model
st.text('Keywords:')
st.text(response["choices"][0]["text"])                                  # displaying the output for the user to see the extracted keywords
