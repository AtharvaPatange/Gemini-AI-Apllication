# # Use a pipeline as a high-level helper
# from transformers import pipeline


# # Load a pretrained image classification pipeline
# # Use an actual model from Hugging Face (example: "microsoft/resnet-50" for image classification)
# detector = pipeline("image-classification", model="facebook/detectron2",device=0,trust_remote_code=True) # Replace with the actual model

# # Analyze an image
# image_path = r"C:\Users\HP\Downloads\newfake.webp" # Replace with the path to your image
# result = detector(image_path)

# # Print the result
# print(result)


# from transformers import AutoModelForObjectDetection, AutoProcessor, pipeline

# model_name = "hustvl/yolos-tiny"
# model = AutoModelForObjectDetection.from_pretrained(model_name)
# processor = AutoProcessor.from_pretrained(model_name)

# object_detector = pipeline("object-detection", model=model, processor=processor)
# results = object_detector(r"C:\Users\HP\Downloads\newfake.webp")

# print(results)


# from transformers import AutoModelForObjectDetection, AutoImageProcessor, pipeline

# # Load the model and image processor
# model_name = "hustvl/yolos-tiny"
# model = AutoModelForObjectDetection.from_pretrained(model_name)
# processor = AutoImageProcessor.from_pretrained(model_name)

# # Create the object detection pipeline
# object_detector = pipeline("object-detection", model=model, image_processor=processor)

# # Run detection on an image
# image_path = r"C:\Users\HP\Pictures\fake.jpg"
# results = object_detector(image_path)

# print(results)




# from transformers import AutoModelForImageClassification, AutoImageProcessor, pipeline
# from PIL import Image

# # Load the model and image processor
# model_name = "Wvolf/ViT_Deepfake_Detection"
# model = AutoModelForImageClassification.from_pretrained(model_name)
# processor = AutoImageProcessor.from_pretrained(model_name)

# # Create the image classification pipeline
# deepfake_detector = pipeline("image-classification", model=model, feature_extractor=processor)

# # Load and preprocess the image
# image_path = r"C:\Users\HP\Pictures\real.jpg"
# image = Image.open(image_path)

# # Run detection
# results = deepfake_detector(image)

# print(results)




# import matplotlib.pyplot as plt
# from transformers import AutoModelForImageClassification, AutoImageProcessor, pipeline
# from PIL import Image

# # Load the model and image processor
# model_name = "Wvolf/ViT_Deepfake_Detection"
# model = AutoModelForImageClassification.from_pretrained(model_name)
# processor = AutoImageProcessor.from_pretrained(model_name)

# # Create the image classification pipeline
# deepfake_detector = pipeline("image-classification", model=model, feature_extractor=processor)

# # Load and preprocess the image
# image_path = r"C:\Users\HP\Pictures\real.jpg"  # Change this to your image path
# image = Image.open(image_path)

# # Run detection
# results = deepfake_detector(image)

# # Extract scores and labels
# labels = [result["label"] for result in results]
# scores = [result["score"] for result in results]

# # Plot bar chart
# plt.figure(figsize=(6, 4))
# plt.bar(labels, scores, color=['green' if label == 'real' else 'red' for label in labels])
# plt.xlabel("Prediction")
# plt.ylabel("Confidence Score")
# plt.ylim(0, 1)  # Confidence score is between 0 and 1
# plt.title("Deepfake Detection Confidence")
# plt.show()



# import matplotlib.pyplot as plt
# from transformers import AutoModelForImageClassification, AutoImageProcessor, pipeline
# from PIL import Image

# # Load the model and image processor
# model_name = "Wvolf/ViT_Deepfake_Detection"
# model = AutoModelForImageClassification.from_pretrained(model_name)
# processor = AutoImageProcessor.from_pretrained(model_name)

# # Create the image classification pipeline
# deepfake_detector = pipeline("image-classification", model=model, feature_extractor=processor)

# # Load and preprocess the image
# image_path = r"C:\Users\HP\Pictures\real.jpg"  # Change this to your image path
# image = Image.open(image_path)

# # Run detection
# results = deepfake_detector(image)

# # Extract scores and labels
# labels = [result["label"].capitalize() for result in results]  # Capitalize 'real' or 'fake'
# scores = [result["score"] for result in results]

# # Define fresh, vibrant colors
# colors = ['#00FF00' if label == 'Real' else '#FF4500' for label in labels]  # Bright green for real, bright orange-red for fake

# # 3D Effect using explode
# explode = [0.1 if label == 'Fake' else 0 for label in labels]  # Slightly explode 'Fake' section for emphasis

# # Plot the 3D Pie Chart
# plt.figure(figsize=(7, 7))
# plt.pie(scores, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140, 
#         wedgeprops={'edgecolor': 'black', 'linewidth': 1.5}, explode=explode, shadow=True)
# plt.title("Deepfake Detection Confidence", fontsize=14, fontweight='bold')

# # Show the chart
# plt.show()


import os
import requests
from io import BytesIO
from flask import Flask, request, jsonify, send_file
from transformers import AutoModelForImageClassification, AutoImageProcessor, pipeline
from PIL import Image
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load the deepfake detection model
model_name = "Wvolf/ViT_Deepfake_Detection"
model = AutoModelForImageClassification.from_pretrained(model_name)
processor = AutoImageProcessor.from_pretrained(model_name)
deepfake_detector = pipeline("image-classification", model=model, feature_extractor=processor)

# Folder to save pie chart images
if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/detect", methods=["POST"])
def detect_deepfake():
    data = request.get_json()  # Accept JSON data
    image_url = data.get("image_url")
    
    if not image_url:
        return jsonify({"error": "No image URL provided"}), 400

    try:
        # Download the image from the URL
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))

        # Run deepfake detection
        results = deepfake_detector(image)
        
        output = [
            {"label": result["label"], "score": round(result["score"], 3)} for result in results
        ]

        

        
        return jsonify({
            "result": output,
           
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
