
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# function to load google gemini model

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt[0], question])
    return response.text






st.set_page_config(page_title="Text to SQL", page_icon="🔍")
st.header("Gemini App to retrieve SQL data")
