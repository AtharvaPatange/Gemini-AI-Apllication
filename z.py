from groq import Groq
import os
import requests
from flask_cors import CORS
from flask import Flask, jsonify, request, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for session management
CORS(app)

API_KEY_LLAMA = "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"

# Dictionary to store conversation history for each user
conversation_history = {}

def generate_llama_response(context, prompt, conversation_history):
    # Construct conversation history string
    history_text = "\n".join([f"User: {msg['user']}\nAI: {msg['ai']}" 
                             for msg in conversation_history])
    
    pre_defined = f"""You will receive user's medical history: {context}

Previous conversation history:
{history_text}

Current user question: {prompt}

You are a professional doctor, please assist the user with their question while taking into account their medical history and previous conversation context.
"""
    
    client = Groq(api_key=API_KEY_LLAMA)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": pre_defined}],
        model="llama3-8b-8192",
    )
    return response.choices[0].message.content

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    
    if not all(key in data for key in ['prompt', 'user_data', 'user_id']):
        return jsonify({
            "error": "Invalid input. Please provide 'prompt', 'user_data', and 'user_id' in JSON format."
        }), 400

    query = data['prompt']
    user_data = data['user_data']
    user_id = data['user_id']

    # Initialize conversation history for new users
    if user_id not in conversation_history:
        conversation_history[user_id] = []

    # Get response from LLM
    response = generate_llama_response(
        user_data, 
        query, 
        conversation_history[user_id]
    )

    # Add the current conversation to history
    conversation_history[user_id].append({
        'user': query,
        'ai': response,
        'timestamp': datetime.now().isoformat()
    })

    # Keep only last N conversations (e.g., last 10)
    MAX_HISTORY = 10
    if len(conversation_history[user_id]) > MAX_HISTORY:
        conversation_history[user_id] = conversation_history[user_id][-MAX_HISTORY:]

    return jsonify({
        "response": response,
        "conversation_history": conversation_history[user_id]
    })

# Optional: Endpoint to get conversation history
@app.route('/get_history/<user_id>', methods=['GET'])
def get_history(user_id):
    if user_id not in conversation_history:
        return jsonify({"error": "No history found for this user"}), 404
    return jsonify({"history": conversation_history[user_id]})

# Optional: Endpoint to clear conversation history
@app.route('/clear_history/<user_id>', methods=['POST'])
def clear_history(user_id):
    if user_id in conversation_history:
        conversation_history[user_id] = []
    return jsonify({"message": "Conversation history cleared"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)