# from dotenv import load_dotenv
# load_dotenv() ## loading all the environment variables

# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## function to load Gemini Pro model and get repsonses
# model=genai.GenerativeModel("gemini-pro") 
# chat = model.start_chat(history=[])
# def get_gemini_response(question):
    
#     response=chat.send_message(question,stream=True)
#     return response

# ##initialize our streamlit app

# st.set_page_config(page_title="Q&A Demo")

# st.header("AI recipe builder")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input=st.text_input("Input: ",key="input")
# submit=st.button("Ask the question")

# if submit and input:
#     response=get_gemini_response(input)
#     # Add user query and response to session state chat history
#     st.session_state['chat_history'].append(("You", input))
#     st.subheader("The Response is")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Bot", chunk.text))
# st.subheader("The Chat History is")
    
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")

# import streamlit as st
# from PIL import Image
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure Google Generative AI
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Load Gemini Pro model for text input
# text_model = genai.GenerativeModel("gemini-pro")

# # Load another model for image input (assuming "gemini-1.5-flash" supports image input)
# image_model = genai.GenerativeModel("gemini-1.5-flash")

# def get_text_response(question):
#     chat = text_model.start_chat(history=[])
#     response = chat.send_message(question, stream=True)
#     return response

# def get_image_response(input_prompt, image):
#     if input_prompt:
#         response = image_model.generate_content([input_prompt, image])
#     else:
#         response = image_model.generate_content(image)
#     return response.text

# # Initialize Streamlit app
# st.set_page_config(page_title="AI Recipe and Q&A Demo")

# st.header("AI Recipe Builder and Q&A")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# # User input and image upload
# input_prompt = st.text_input("Ask or Input: ", key="input_prompt")
# uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

# image = None
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)

# # Buttons for specific actions
# submit_recipe = st.button("Tell me the recipe")
# submit_general = st.button("Submit General Input")

# # Process user input based on the button clicked
# if submit_recipe and uploaded_file:
#     recipe_prompt = '''
#     You are a Master chef who knows recipes from all over the world: Indian, Italian, American, Russian, Brazilian, etc. Now:
#     Analyze the uploaded image of the recipe and provide detailed information as follows:
#     1. **List of Ingredients:** Identify and list all the items visible in the image.
#     2. **Recipe Instructions:** Generate a step-by-step recipe for preparing the dish shown in the image.
#     3. **Preparation Method:** Describe the method for making the recipe, including any specific techniques or processes involved.
#     4. **Precautions:** Mention any precautions or tips that should be considered while preparing the dish.
#     Ensure the information is clear, comprehensive, and easy to follow.
#     '''
#     response = get_image_response(recipe_prompt, image)
#     st.session_state['chat_history'].append(("You", "Tell me the recipe"))
#     st.session_state['chat_history'].append(("Bot", response))
#     st.subheader("The Recipe is")
#     st.write(response)
# elif submit_general and input_prompt:
#     response = get_text_response(input_prompt)
#     st.session_state['chat_history'].append(("You", input_prompt))
#     st.subheader("The Response is")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Bot", chunk.text))

# st.subheader("The Chat History is")
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")

from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
import subprocess

# Start the Flask app
subprocess.Popen(['python', 'api.py'])

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="MyGPT")
st.header("AI Recipe Builder")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Send")

if submit and input:
    response = get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
