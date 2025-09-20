
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

import google.generativeai as genai
import sqlite3
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# function to load google gemini model

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([prompt[0], question])
    return response.text


# function to retrieve data from sqlite database


def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


prompt = [
    """
    You are an expert in converting English questions to SQL code!
    The SQL database has the name STUDENT and has the following columns - NAME, PROGRAM, SECTION. \n\n
    For example, 
    \n example 1 - How many entries of records are present? ,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT
    \n example 2 - give me all students studying in Data Science class? ,
    the SQL command will be something like this SELECT * FROM STUDENT where PROGRAM='Data science'
    Also the SQL code should not have ``` in beginning or end and sql word in output.
    """
]


st.set_page_config(page_title="Text to SQL", page_icon="🔍")
st.header("Gemini App to retrieve SQL data")


question = st.text_input("Input: ", key="input")
submit = st.button("Submit")

if submit:
    result = get_gemini_response(question, prompt)
    response = read_sql_query(result, "student.db")
    st.subheader("Output:")
    for row in response:
        st.header(row)
