from flask import Flask, request, jsonify
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question,session_id):
    response = chat.send_message(question, stream=True)
    return response

@app.route('/api/chat', methods=['POST'])
def chat_endpoint():
    data = request.json
    session_id=data.get('sessionID')
    question = data.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400

    response = get_gemini_response(question)
    response_text = ''.join([chunk.text for chunk in response])
    
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(port=5000)
