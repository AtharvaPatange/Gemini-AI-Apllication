

# from flask import Flask, request, jsonify
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()  # Load environment variables

# app = Flask(__name__)

# # Configure the Gemini API
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Load the model outside the function to avoid reloading it each time
# model = genai.GenerativeModel("gemini-pro")

# def get_gemini_response(question, prompt=None):
#     # If a prompt is not provided, set it to an empty string
#     prompt = prompt if prompt else ""
#     # Generate response from the model
#     response = model.generate_content([question, prompt])
    
    
#     return response.text

# @app.route('/api/chat', methods=['POST'])
# def chat_endpoint():
#     data = request.json
    
#     question = data.get('question')
#     prompt = data.get('prompt')  # Optional prompt

#     if not question:
#         return jsonify({"error": "No question provided"}), 400

#     # Get the Gemini model response
#     response_text = get_gemini_response(question, prompt)
    
#     return jsonify({"response": response_text})

# if __name__ == '__main__':
#     app.run(port=5000)


from flask import Flask, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv
import random  

load_dotenv() 

app = Flask(__name__)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


PREDEFINED_PROMPTS = [
    "Provide detailed guidance based on the following context:",
    "Analyze the following question and provide an in-depth response:",
    "Generate content that helps answer this question:",
    "Using your knowledge, provide a comprehensive answer to the query:"
]

def get_gemini_response(question):
   
    prompt = random.choice(PREDEFINED_PROMPTS)   
    response = model.generate_content([question, prompt])
    return response.text

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    
    question = data.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

   
    response_text = get_gemini_response(question)
    
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(port=5000)
