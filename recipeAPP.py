import google.generativeai as genai
import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_prompt, image):
    if input_prompt:
        response = model.generate_content([input_prompt, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.header("AI Recipe Builder")

# User input and image upload
general_input = st.text_input("Ask or Input: ", key="general_input")
uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Buttons for specific actions
submit_recipe = st.button("Tell me the recipe")
submit_general = st.button("Submit General Input")

# If "Tell me the recipe" button is clicked
if submit_recipe:
    if uploaded_file is not None:
        recipe_prompt = '''
        You are a Master chef who knows recipes from all over the world: Indian, Italian, American, Russian, Brazilian, etc. Now:
        Analyze the uploaded image of the recipe and provide detailed information as follows:
        1. **List of Ingredients:** Identify and list all the items visible in the image.
        2. **Recipe Instructions:** Generate a step-by-step recipe for preparing the dish shown in the image.
        3. **Preparation Method:** Describe the method for making the recipe, including any specific techniques or processes involved.
        4. **Precautions:** Mention any precautions or tips that should be considered while preparing the dish.
        Ensure the information is clear, comprehensive, and easy to follow.
        '''
        response = get_gemini_response(recipe_prompt, image)
        st.subheader("The Recipe is")
        st.write(response)
    else:
        st.write("Please upload an image to get the recipe.")

# If "Submit General Input" button is clicked
if submit_general:
    if general_input:
        response = get_gemini_response(general_input, "")
        st.subheader("Response to General Input")
        st.write(response)
    else:
        st.write("Please enter your query or input.")

