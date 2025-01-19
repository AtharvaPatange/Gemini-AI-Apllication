from flask import Flask, request, jsonify
import ephem
from datetime import datetime
from flask_cors import CORS  # Import CORS
# Flask app initialization
app = Flask(__name__)

CORS(app)



import requests
from groq import Groq
api_key_llama = "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"  


def generate_llama_response(predefined_prompt, api_key):
    prompt = predefined_prompt

   
    client = Groq(api_key=api_key)

 
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192", 
    )
    
    llama_response_content = response.choices[0].message.content
 
    return llama_response_content


    
# Function to generate personalized spiritual advice using GPT
def get_spiritual_advice(name, dob, kundali):
    prompt=f"""
    User Details:
    Name: {name}
    Date of Birth: {dob}
    Kundali: {kundali}
    
   Provide spiritual guidance based on the user's birth chart. Include:
    1. insights on career, relationships, personal growth, family, and social connections. Daily and monthly horoscopes.
    2. Recommendations for gemstones.
    3. Rituals to improve well-being.
    4. Do's and Don'ts.
    5. Meditation and workout suggestions aligned with horoscope insights.
    6.Sleep content tailored to user needs.

    """


    client = Groq(api_key=api_key_llama)

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192", 
    )
    
    llama_response_content = response.choices[0].message.content
 
    return llama_response_content
 
# Flask route to handle user input
@app.route('/chat', methods=['POST'])
def soulbuddy():
    try:
        
        data = request.json
        
       
        user_data = {
            "name": data.get("name"),
            "dob": data.get("dob"),
            "time": data.get("time"),
            "city": data.get("city"),
        }
        
         # Validate input
        if not all([user_data["name"], user_data["dob"], user_data["time"], user_data["city"]]):
            return jsonify({"error": "Missing required fields (name, dob, time, city)"}), 400

        response = requests.post('https://gemini-ai-apllication.onrender.com/soulbuddy1', json=user_data)

        # if response.status_code == 200:
        # Retrieve the response as text
        kundali = response.text
        spiritual_advice = get_spiritual_advice(
                user_data["name"], 
                user_data["dob"], 
                kundali
            )

        return jsonify({"spiritual_advice": spiritual_advice})
        # else:
        #   return jsonify({"error": f"Failed to fetch data. Status Code: {response.status_code}"}), 400
       
       
    

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True,port=8000)






