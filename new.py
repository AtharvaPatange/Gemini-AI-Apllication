from flask import Flask, request, jsonify
import ephem
from datetime import datetime
from flask_cors import CORS  # Import CORS
# Flask app initialization
app = Flask(__name__)

CORS(app)


# Helper function for astrological insights using PyEphem
# def generate_kundali(name, dob, time, city):
#     # Combine date and time
#     birth_datetime = datetime.strptime(f"{dob} {time}", "%Y-%m-%d %H:%M")
#     observer = ephem.Observer()

#     # Sample city coordinates (update based on actual location)
#     city_coordinates = {
#         "Mumbai": (19.0760, 72.8777),
#         "Delhi": (28.6139, 77.2090),
#     }
#     if city not in city_coordinates:
#         return {"error": "City not supported"}

#     observer.lat, observer.lon = city_coordinates[city]
#     observer.date = birth_datetime

#     # Planetary positions
#     planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
#     kundali = {}
#     for planet in planets:
#         planet_ephem = getattr(ephem, planet)()
#         planet_ephem.compute(observer)
#         kundali[planet] = {
#             "position": f"{planet_ephem.ra} RA / {planet_ephem.dec} DEC",
#             "house": f"{int(planet_ephem.ra / (360 / 12)) + 1}th house",
#         }
#     return kundali

# print(generate_kundali(name="Atharva",dob="2000-01-01",city="Mumbai",time="6:00"))

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
    1. Recommendations for gemstones.
    2. Rituals to improve well-being.
    3. Do's and Don'ts.
    """
    # if query:
    #     prompt += f" User Query: {query}"

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

        response = requests.post('http://127.0.0.1:5000/soulbuddy1', json=user_data)

        if response.status_code == 200:
        # Retrieve the response as text
          kundali = response.text
          spiritual_advice = get_spiritual_advice(
                user_data["name"], 
                user_data["dob"], 
                kundali
            )

          return jsonify({"spiritual_advice": spiritual_advice})
        else:
          return jsonify({"error": f"Failed to fetch data. Status Code: {response.status_code}"}), 400
       
       
    

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True,port=8000)











def get_spiritual_advice(name, dob, kundali, query=None):
    prompt=f"""
    User Details:
    Name: {name}
    Date of Birth: {dob}
    Kundali: {kundali}
    
   Provide spiritual guidance based on the user's birth chart. Include:
    1. Recommendations for gemstones.
    2. Rituals to improve well-being.
    3. Do's and Don'ts.
    """
    if query:
        prompt += f" User Query: {query}"

    client = Groq(api_key=api_key_llama)

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama3-8b-8192", 
    )
    
    llama_response_content = response.choices[0].message.content
 
    return llama_response_content


# def generate_llama_response(predefined_prompt, api_key):
#     prompt = predefined_prompt

   
#     client = Groq(api_key=api_key)

 
#     response = client.chat.completions.create(
#         messages=[{"role": "user", "content": prompt}],
#         model="llama3-8b-8192", 
#     )
    
#     llama_response_content = response.choices[0].message.content
 
#     return llama_response_content



# from flask import Flask, request, jsonify
# import openai
# import numpy as np
# from datetime import datetime

# # Flask app initialization
# app = Flask(__name__)



# def deg_to_rad(deg):
#     return deg * (np.pi / 180)

# def rad_to_deg(rad):
#     return rad * (180 / np.pi)

# # Helper function for astrological insights using NumPy
# def generate_kundali_with_numpy(name, dob, time, city):
#     # Combine date and time
#     birth_datetime = datetime.strptime(f"{dob} {time}", "%Y-%m-%d %H:%M")

#     # City coordinates (latitude, longitude)
#     city_coordinates = {
#         "Mumbai": (19.0760, 72.8777),
#         "Delhi": (28.6139, 77.2090),
#     }
#     if city not in city_coordinates:
#         return {"error": "City not supported"}

#     lat, lon = city_coordinates[city]

#     # Calculate sidereal time
#     jd = birth_datetime.toordinal() + 1721424.5  # Julian date
#     t = (jd - 2451545.0) / 36525.0  # Julian centuries from J2000.0
#     sidereal_time = (280.46061837 + 360.98564736629 * (jd - 2451545.0) + 0.000387933 * t ** 2 - t ** 3 / 38710000.0) % 360

#     # Adjust for longitude
#     local_sidereal_time = (sidereal_time + lon) % 360

#     # Planetary positions (simplified for demo purposes)
#     planets = {
#         "Sun": (np.sin(deg_to_rad(t * 360)) * 23.44, "RA"),
#         "Moon": (np.sin(deg_to_rad(t * 13.176396)) * 5.14, "RA"),
#         "Mercury": (np.sin(deg_to_rad(t * 4.092334)) * 7.0, "RA"),
#         "Venus": (np.sin(deg_to_rad(t * 1.602130)) * 3.39, "RA"),
#         "Mars": (np.sin(deg_to_rad(t * 0.524032)) * 1.85, "RA"),
#         "Jupiter": (np.sin(deg_to_rad(t * 0.083056)) * 1.31, "RA"),
#         "Saturn": (np.sin(deg_to_rad(t * 0.033456)) * 2.49, "RA"),
#     }

#     # Generate houses based on local sidereal time
#     houses = {}
#     for i in range(1, 13):
#         houses[f"House {i}"] = (local_sidereal_time + (i - 1) * 30) % 360

#     kundali = {
#         "planets": {planet: {"position": rad_to_deg(pos[0]), "type": pos[1]} for planet, pos in planets.items()},
#         "houses": houses,
#     }

#     return kundali

# # Function to generate personalized spiritual advice using GPT
# def get_spiritual_advice(name, dob, kundali, query=None):
#     prompt = f"""
#     User Details:
#     Name: {name}
#     Date of Birth: {dob}
#     Kundali: {kundali}

#     Provide spiritual guidance based on the user's birth chart. Include:
#     1. Recommendations for gemstones.
#     2. Rituals to improve well-being.
#     3. Do's and Don'ts.
#     """
#     if query:
#         prompt += f" User Query: {query}"

#     client = Groq(api_key=api_key_llama)

#     response = client.chat.completions.create(
#         messages=[{"role": "user", "content": prompt}],
#         model="llama3-8b-8192", 
#     )
    
#     llama_response_content = response.choices[0].message.content
 
#     return llama_response_content

# # Flask route to handle user input
# @app.route('/soulbuddy', methods=['POST'])
# def soulbuddy():
#     try:
#         data = request.json
#         name = data.get("name")
#         dob = data.get("dob")  # Format: YYYY-MM-DD
#         time = data.get("time")  # Format: HH:MM
#         city = data.get("city")
#         query = data.get("query", None)

#         if not all([name, dob, time, city]):
#             return jsonify({"error": "Missing required fields"}), 400

#         # Generate Kundali
#         kundali = generate_kundali_with_numpy(name, dob, time, city)
#         if "error" in kundali:
#             return jsonify({"error": kundali["error"]}), 400

#         # Get spiritual advice
#         advice = get_spiritual_advice(name, dob, kundali, query)
#         return jsonify({"kundali": kundali, "advice": advice})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)
