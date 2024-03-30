import os
from dotenv import load_dotenv
from openai
import streamlit as st

load_dotenv(".evn")

cilent = OpenAI(
    api_key = st.secrets["OPENAI_API_KEY"]
)

def main():

st.title ('Life of Content')
st.header('AI Creative Idea', divider='rainbow')

user_prompt = st.text_area('Enter a prompt for conten')

options = st.multiselect(
    'What are your favorite type of content',
    ['Life style', 'Education', 'Tranding', 'Aesthetic'],
    ['Life style', 'Aesthetic'])


age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# st.write('You selected:', options)

if __name__ == "__main__":
    main()