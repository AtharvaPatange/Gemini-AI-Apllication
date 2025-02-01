# from transformers import AutoModelForVideoClassification, AutoImageProcessor, pipeline
# import cv2
# import torch
# from PIL import Image
# import numpy as np

# def process_video_for_deepfake_detection(video_path, batch_size=8):
#     # Use Timesformer model which is specifically for video classification
#     model_name = "facebook/timesformer-base-finetuned-k400"
#     processor = AutoImageProcessor.from_pretrained(model_name)
#     model = AutoModelForVideoClassification.from_pretrained(model_name)
    
#     # Create video capture object
#     cap = cv2.VideoCapture(video_path)
#     frames = []
#     predictions = []
    
#     print("Processing video frames...")
    
#     # Get video properties
#     fps = int(cap.get(cv2.CAP_PROP_FPS))
#     frame_count = 0
    
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
            
#         # Process every nth frame to match model's expected frame rate
#         if frame_count % (fps // 4) == 0:  # Process 4 frames per second
#             # Convert BGR to RGB
#             frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             frame_pil = Image.fromarray(frame_rgb)
            
#             # Resize frame to expected size (224x224 is common)
#             frame_pil = frame_pil.resize((224, 224))
#             frames.append(frame_pil)
            
#             # Process when we have enough frames
#             if len(frames) == batch_size:
#                 try:
#                     inputs = processor(frames, return_tensors="pt")
#                     with torch.no_grad():
#                         outputs = model(**inputs)
#                         probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
#                         predictions.append(probs[0].tolist())
#                     frames = []
#                 except Exception as e:
#                     print(f"Error processing batch: {str(e)}")
#                     frames = []
        
#         frame_count += 1
    
#     cap.release()
    
#     if not predictions:
#         return {"error": "No predictions were made"}
    
#     # Average predictions
#     avg_prediction = np.mean(predictions, axis=0)
    
#     # Map the highest probability to fake/real
#     max_prob = max(avg_prediction)
#     is_fake = avg_prediction[0] > 0.5  # Simple threshold
    
#     return {
#         "real_probability": 1 - max_prob if is_fake else max_prob,
#         "fake_probability": max_prob if is_fake else 1 - max_prob
#     }

# # Alternative approach using VisionTransformer
# def detect_deepfake_vit(video_path):
#     from transformers import ViTForImageClassification, ViTImageProcessor
    
#     # Load ViT model
#     model_name = "google/vit-base-patch16-224"
#     processor = ViTImageProcessor.from_pretrained(model_name)
#     model = ViTForImageClassification.from_pretrained(model_name)
    
#     cap = cv2.VideoCapture(video_path)
#     frame_predictions = []
    
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
            
#         # Convert and process frame
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame_pil = Image.fromarray(frame_rgb)
        
#         inputs = processor(images=frame_pil, return_tensors="pt")
        
#         with torch.no_grad():
#             outputs = model(**inputs)
#             probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
#             frame_predictions.append(probs[0].tolist())
    
#     cap.release()
    
#     if not frame_predictions:
#         return {"error": "No frames processed"}
        
#     avg_prediction = np.mean(frame_predictions, axis=0)
#     return {
#         "real_probability": float(avg_prediction[0]),
#         "fake_probability": float(avg_prediction[1])
#     }

# if __name__ == "__main__":
#     video_path = r"C:\Users\HP\Downloads\videoplayback (1).mp4" # Replace with your video path
#     try:
#         print("Starting deepfake detection...")
        
#         # Try both methods
#         results1 = process_video_for_deepfake_detection(video_path)
#         print("\nTimesformer Results:")
#         if "error" in results1:
#             print(f"Error: {results1['error']}")
#         else:
#             print(f"Real Probability: {results1['real_probability']:.2%}")
#             print(f"Fake Probability: {results1['fake_probability']:.2%}")
            
#         print("\nTrying ViT method...")
#         results2 = detect_deepfake_vit(video_path)
#         print("\nViT Results:")
#         if "error" in results2:
#             print(f"Error: {results2['error']}")
#         else:
#             print(f"Real Probability: {results2['real_probability']:.2%}")
#             print(f"Fake Probability: {results2['fake_probability']:.2%}")
            
#     except Exception as e:
#         print(f"Error processing video: {str(e)}")



# # def enhance_video_processing(video_path, skip_frames=5):
# #     """
# #     Enhanced version with frame skipping and face detection
# #     """
# #     import face_recognition  # You'll need to install this package
    
# #     cap = cv2.VideoCapture(video_path)
# #     frames_with_faces = []
    
# #     frame_count = 0
# #     while True:
# #         ret, frame = cap.read()
# #         if not ret:
# #             break
            
# #         # Skip frames to speed up processing
# #         if frame_count % skip_frames != 0:
# #             frame_count += 1
# #             continue
            
# #         # Convert to RGB for face detection
# #         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
# #         # Detect faces
# #         face_locations = face_recognition.face_locations(rgb_frame)
        
# #         # If faces found, process the frame
# #         if face_locations:
# #             frame_pil = Image.fromarray(rgb_frame)
# #             frames_with_faces.append(frame_pil)
        
# #         frame_count += 1
    
# #     cap.release()
# #     return frames_with_faces


# # # Enhanced usage
# # video_path = r"C:\Users\HP\Downloads\reayaz (1).mp4"
# # frames = enhance_video_processing(video_path)
# # results = process_video_for_deepfake_detection(frames)



from flask import Flask, request, jsonify , render_template
import os
from werkzeug.utils import secure_filename
import time

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max-limit
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'wmv'}

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Utility functions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Import your deepfake detection functions
from transformers import AutoModelForVideoClassification, AutoImageProcessor, pipeline
import cv2
import torch
from PIL import Image
import numpy as np

def process_video_for_deepfake_detection(video_path, batch_size=8):
    model_name = "facebook/timesformer-base-finetuned-k400"
    processor = AutoImageProcessor.from_pretrained(model_name)
    model = AutoModelForVideoClassification.from_pretrained(model_name)
    
    cap = cv2.VideoCapture(video_path)
    frames = []
    predictions = []
    
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        if frame_count % (fps // 4) == 0:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_pil = Image.fromarray(frame_rgb)
            frame_pil = frame_pil.resize((224, 224))
            frames.append(frame_pil)
            
            if len(frames) == batch_size:
                try:
                    inputs = processor(frames, return_tensors="pt")
                    with torch.no_grad():
                        outputs = model(**inputs)
                        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
                        predictions.append(probs[0].tolist())
                    frames = []
                except Exception as e:
                    frames = []
        
        frame_count += 1
    
    cap.release()
    
    if not predictions:
        return {"error": "No predictions were made"}
    
    avg_prediction = np.mean(predictions, axis=0)
    max_prob = max(avg_prediction)
    is_fake = avg_prediction[0] > 0.5
    
    return {
        "real_probability": float(1 - max_prob if is_fake else max_prob),
        "fake_probability": float(max_prob if is_fake else 1 - max_prob)
    }

def detect_deepfake_vit(video_path):
    from transformers import ViTForImageClassification, ViTImageProcessor
    
    model_name = "google/vit-base-patch16-224"
    processor = ViTImageProcessor.from_pretrained(model_name)
    model = ViTForImageClassification.from_pretrained(model_name)
    
    cap = cv2.VideoCapture(video_path)
    frame_predictions = []
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_pil = Image.fromarray(frame_rgb)
        
        inputs = processor(images=frame_pil, return_tensors="pt")
        
        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
            frame_predictions.append(probs[0].tolist())
    
    cap.release()
    
    if not frame_predictions:
        return {"error": "No frames processed"}
        
    avg_prediction = np.mean(frame_predictions, axis=0)
    return {
        "real_probability": float(avg_prediction[0]),
        "fake_probability": float(avg_prediction[1])
    }

@app.route('/')
def home():
    return render_template('index.html')
# API Routes
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Service is running"})

@app.route('/detect-deepfake', methods=['POST'])
def detect_deepfake():
    try:
        # Check if video file is present in request
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400
        
        file = request.files['video']
        
        # Check if a file was actually selected
        if file.filename == '':
            return jsonify({'error': 'No video file selected'}), 400
        
        # Check if file type is allowed
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400
        
        # Save the file
        filename = secure_filename(file.filename)
        timestamp = str(int(time.time()))
        filename = f"{timestamp}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Process the video
        try:
            # Try both methods
            results1 = process_video_for_deepfake_detection(filepath)
            results2 = detect_deepfake_vit(filepath)
            
            # Combine results
            combined_results = {
                "timesformer_results": results1,
                "vit_results": results2
            }
            
            # Clean up
            os.remove(filepath)
            
            return jsonify({
                "status": "success",
                "results": combined_results
            })
            
        except Exception as e:
            # Clean up in case of error
            if os.path.exists(filepath):
                os.remove(filepath)
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500
            
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# Error handlers
@app.errorhandler(413)
def too_large(e):
    return jsonify({
        "status": "error",
        "message": "File is too large"
    }), 413

@app.errorhandler(500)
def internal_error(e):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)