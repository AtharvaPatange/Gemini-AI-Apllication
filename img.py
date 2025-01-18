# Use a pipeline as a high-level helper
from transformers import pipeline



# Load a pretrained image classification pipeline
# Use an actual model from Hugging Face (example: "microsoft/resnet-50" for image classification)
detector = pipeline("image-classification", model="deepseek-ai/DeepSeek-V3",device=0,trust_remote_code=True) # Replace with the actual model

# Analyze an image
image_path = r"C:\Users\HP\Downloads\newfake.webp" # Replace with the path to your image
result = detector(image_path)

# Print the result
print(result)
