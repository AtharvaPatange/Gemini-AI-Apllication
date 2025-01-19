from flask import Flask, request, jsonify
import ephem
from datetime import datetime
from flask_cors import CORS

# Flask app initialization
app = Flask(__name__)

CORS(app)

# Helper function for astrological insights using PyEphem
def generate_kundali(name, dob, time, city):
    # Combine date and time
    birth_datetime = datetime.strptime(f"{dob} {time}", "%Y-%m-%d %H:%M")
    observer = ephem.Observer()

    # Sample city coordinates (update based on actual location)
    city_coordinates = {
        "Mumbai": (19.0760, 72.8777),
        "Delhi": (28.6139, 77.2090),
        "Pune":  (18.5204, 73.8567),
        "Hyderabad": (17.3850, 78.4866),
        "Banglore":  (12.9715, 77.5945),     
        "Mumbai": (19.0760, 72.8777),
        "Delhi": (28.7041, 77.1025),
    "Bengaluru": (12.9716, 77.5946),
    "Kolkata": (22.5726, 88.3639),
    "Chennai": (13.0827, 80.2707),
    "Hyderabad": (17.3850, 78.4867),
    "Pune": (18.5204, 73.8567),
    "Ahmedabad": (23.0225, 72.5714),
    "Jaipur": (26.9124, 75.7873),
    "Lucknow": (26.8467, 80.9462),
    "Kanpur": (26.4499, 80.3319),
    "Nagpur": (21.1458, 79.0882),
    "Indore": (22.7196, 75.8577),
    "Bhopal": (23.2599, 77.4126),
    "Patna": (25.5941, 85.1376),
    "Thiruvananthapuram": (8.5241, 76.9366),
    "Kochi": (9.9312, 76.2673),
    "Surat": (21.1702, 72.8311),
    "Vadodara": (22.3072, 73.1812),
    "Ranchi": (23.3441, 85.3096),
    "Guwahati": (26.1445, 91.7362),
    "Shimla": (31.1048, 77.1734),
    "Chandigarh": (30.7333, 76.7794),
    "Varanasi": (25.3176, 82.9739),
    "Amritsar": (31.6340, 74.8723)

        
    }
    if city not in city_coordinates:
        return {"error": "City not supported"}

    observer.lat, observer.lon = city_coordinates[city]
    observer.date = birth_datetime

    # Planetary positions
    planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
    kundali = []
    for planet in planets:
        planet_ephem = getattr(ephem, planet)()
        planet_ephem.compute(observer)
        ra_deg = planet_ephem.ra * 180 / 3.14159  # Convert RA to degrees
        dec_deg = planet_ephem.dec * 180 / 3.14159  # Convert Dec to degrees
        house = (int(ra_deg / (360 / 12)) + 1) % 12 + 1  # Calculate house

        kundali.append({
            "Planet": planet,
            "RA (Degrees)": f"{ra_deg:.2f}",
            "Dec (Degrees)": f"{dec_deg:.2f}",
            "House": f"{house}th House"
        })
    
    return kundali



# Flask route to handle user input
@app.route('/soulbuddy1', methods=['POST'])
def soulbuddy():
    try:
        data = request.json
        name = data.get("name")
        dob = data.get("dob")  # Format: YYYY-MM-DD
        time = data.get("time")  # Format: HH:MM
        city = data.get("city")
      

        if not all([name, dob, time, city]):
            return jsonify({"error": "Missing required fields"}), 400

        # Generate Kundali
        kundali = generate_kundali(name, dob, time, city)
        if "error" in kundali:
            return jsonify({"error": kundali["error"]}), 400

        # # Get spiritual advice
        # advice = get_spiritual_advice(name, dob, kundali, query)
        return jsonify({"kundali": kundali})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
