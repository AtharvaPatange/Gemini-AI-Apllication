import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure the Gemini AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini model and get response
model = genai.GenerativeModel("gemini-1.5-flash")

def get_geminiai_response(input,image):
    if input!="":
            response=model.generate_content([input,image])
    else:
          response=model.generate_content(image)
    return response.text
   
# initialize you streamlit app

st.set_page_config(page_title="Image to Text")

st.header("AI application")
input=st.text_input("Input: ",key="input")

uploaded_file = st.file_uploader("Upload an image...",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
      image=Image.open(uploaded_file)
      st.image(image,caption="Uploaded Image.",use_column_width=True)


submit=st.button("Tell me about it")

#if submit is clicked
if submit:
    response=get_geminiai_response(input,image)
    st.subheader("The response is")
    st.write(response)