import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Gemini AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get response
model = genai.GenerativeModel("gemini-pro")

def get_geminiai_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Ask a question",page_icon="🦈")

st.header("Gemini AI Application")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Go on")

# When submit is clicked
if submit:
    response = get_geminiai_response(input_text)
    st.write(response)
