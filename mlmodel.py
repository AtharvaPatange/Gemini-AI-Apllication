# from tensorflow.keras.models import load_model
# import numpy as np
# import cv2
# model = load_model(r"C:\Users\HP\Downloads\xray_pneumonia_model.keras")

# def predict_xray(image_path):
#     img = cv2.imread(image_path)
#     img = cv2.resize(img, (150,150))
#     img = img / 255.0
#     img = np.expand_dims(img, axis=0)

#     prediction = model.predict(img)[0][0]
#     return "Pneumonia" if prediction > 0.5 else "Normal"

# # Test with new image
# print(predict_xray(r"C:\Users\HP\Downloads\person100_bacteria_475.jpeg"))





# from flask import Flask, request, jsonify
# from tensorflow.keras.models import load_model

# import numpy as np
# import cv2
# from flask_cors import CORS

# # Load the model
# model = load_model(r"C:\Users\HP\Downloads\xray_pneumonia_model.keras")

# # Initialize Flask app
# app = Flask(__name__)
# CORS(app)
# # Define the prediction function
# def predict_xray(image_path):
#     img = cv2.imread(image_path)
#     if img is None:
#         raise ValueError("Image not found or invalid file path")
#     img = cv2.resize(img, (150, 150))
#     img = img / 255.0
#     img = np.expand_dims(img, axis=0)

#     prediction = model.predict(img)[0][0]
#     return "Pneumonia" if prediction > 0.5 else "Normal"

# # Define the /model route
# @app.route('/model', methods=['POST'])
# def model_predict():
#     # Get JSON data from the request body
#     data = request.get_json()

#     # Check if the file path is provided
#     if not data or 'file_path' not in data:
#         return jsonify({"error": "No file path provided"}), 400

#     file_path = data['file_path']

#     # Make a prediction
#     try:
#         result = predict_xray(file_path)
#         return jsonify({"prediction": result})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # Run the Flask app
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000)


from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import requests
from io import BytesIO
from flask_cors import CORS

# Load the model
model = load_model(r"C:\Users\HP\Downloads\xray_pneumonia_model.keras")

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define the prediction function
def predict_xray(image_source):
    # Check if the source is a URL
    if image_source.startswith("http"):
        response = requests.get(image_source)
        if response.status_code != 200:
            raise ValueError("Failed to fetch image from URL")
        image_array = np.asarray(bytearray(response.content), dtype=np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    else:
        img = cv2.imread(image_source)
        if img is None:
            raise ValueError("Image not found or invalid file path")

    # Preprocess the image
    img = cv2.resize(img, (150, 150))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Make a prediction
    prediction = model.predict(img)[0][0]
    return "Pneumonia" if prediction > 0.5 else "Normal"


from groq import Groq
API_KEY_LLAMA = "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"

def generate_llama_response(result,file_path):
    predefined_prompt=f"You are a X-ray Analyzer you are being provided with X-ray image{file_path} and reslut of it {result} like 'normal' or 'penumonia' you have to assis thye user if penumonia detetcted in just 2 lines "
    client = Groq(api_key=API_KEY_LLAMA)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": predefined_prompt}],
        model="llama3-8b-8192",
    )
    return response.choices[0].message.content


# Define the /model route
@app.route('/model', methods=['POST'])
def model_predict():
    # Get JSON data from the request body
    data = request.get_json()

    # Check if the file path is provided
    if not data or 'file_path' not in data:
        return jsonify({"error": "No file path or URL provided"}), 400

    file_path = data['file_path']

    # Make a prediction
    try:
        result = predict_xray(file_path)
        response=generate_llama_response(result,file_path)
        return jsonify({"prediction": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500




# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
