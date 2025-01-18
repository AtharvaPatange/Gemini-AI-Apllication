from flask import Flask, request, jsonify
import ephem
from datetime import datetime
from waitress import serve

from flask import app 
# Flask app initialization
app = Flask(__name__)

# Helper function for astrological insights using PyEphem
def generate_kundali(name, dob, time, city):
    # Combine date and time
    birth_datetime = datetime.strptime(f"{dob} {time}", "%Y-%m-%d %H:%M")
    observer = ephem.Observer()

    # Sample city coordinates (update based on actual location)
    city_coordinates = {
        "Mumbai": (19.0760, 72.8777),
        "Delhi": (28.6139, 77.2090),
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
