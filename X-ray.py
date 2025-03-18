from transformers import CLIPProcessor, CLIPModel, pipeline
from PIL import Image


clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")



from groq import Groq
API_KEY_LLAMA = "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"

def generate_llama_response(predefined_prompt):
    client = Groq(api_key=API_KEY_LLAMA)
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": predefined_prompt}],
        model="llama3-8b-8192",
    )
    return response.choices[0].message.content

def analyze_xray(image_path):
    
    image = Image.open(image_path)
    inputs = clip_processor(text=["a chest X-ray"], images=image, return_tensors="pt", padding=True)
    

    outputs = clip_model(**inputs)
    image_features = outputs.image_embeds
    
    prompt = f"The X-ray image is provided analyze it {image_path} "
    explanation = generate_llama_response(prompt)
    
    return explanation

image_path =r"C:\Users\HP\Downloads\depositphotos_61211631-stock-photo-fracture-shaft-of-ulnarforearms-bone.jpg"
explanation = analyze_xray(image_path)
print("LLM Explanation:", explanation)