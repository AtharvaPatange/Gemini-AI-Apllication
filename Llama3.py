# import os
# from groq import Groq

# # Initialize the client
# # client = Groq(
# #     api_key=os.environ.get("GROQ_API_KEY"),
# # )
# client = Groq(api_key="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")


# # Take user input dynamically
# user_input = input("Enter your question or message: ")

# # Create a chat completion request
# chat_completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": user_input,
#         }
#     ],
#     model="llama3-8b-8192",
# )

# # Print the response from the model
# print("Response:", chat_completion.choices[0].message.content)



from groq import Groq
import os
import requests
from flask_cors import CORS
from flask import Flask,jsonify,request

app = Flask(__name__)

CORS(app)

API_KEY_LLAMA = "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"

def generate_llama_response(prompt):
    pre_defined=f""" User promt:{prompt}
    You are Solar Nova Assistant, an expert chatbot designed to provide accurate and helpful information about solar energy and the Solar Nova website. Your role is to assist users by answering their queries about website functionalities, the benefits of solar energy, cost estimation, and the detailed process of solar panel installation in India.
Explain users ask about:
    Website Features: Explain tools like the estimation calculator, dashboard, maintenance management, and customer feedback system.
    Solar Energy Benefits: Highlight environmental impact, cost savings, energy independence, and technological advancements.
    Cost Estimation & Calculations: Guide users through the estimation tool by asking relevant inputs like energy usage, roof area, and sunlight exposure. Provide cost breakdowns and payback period insights.
    Installation Process: Explain the step-by-step procedure of solar panel installation on a home roof, including site assessment, design, permits, installation, and maintenance.
    General Solar Queries: Provide insights into solar panel efficiency, performance factors, battery storage, and financial incentives.
Always be concise, informative, and engaging. If a user asks for a cost estimate, guide them to input necessary data and calculate the expected cost using predefined logic. Ensure clarity, avoid technical jargon unless requested, and offer follow-ups for better assistance.
"""
    
    client = Groq(api_key=API_KEY_LLAMA)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": pre_defined}],
        model="llama3-8b-8192",
    )
    return response.choices[0].message.content



@app.route('/chat', methods=['POST'])

def chat():
    data=request.get_json()
    if not 'prompt' in data:
        return jsonify({"error": "Invalid input. Please provide 'user_data' in JSON format."}), 400

    query = data['prompt']
   
    response=generate_llama_response(query)
    

    return jsonify({"response": response})



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=True)
