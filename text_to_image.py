# import time
# import json
# from pathlib import Path
# from urllib.request import urlretrieve

# import requests
# import streamlit as st

# # Set your API key (Replace with your actual API key)
# API_KEY = "de29e160-5bf0-11ef-a4dd-172f678d9c1e"

# # Function to process the image using the Deep Image AI API
# def process_image(file, enhancements=["denoise", "deblur", "light"], width=2000):
#     headers = {
#         'x-api-key': API_KEY,
#     }
#     data = {
#         "enhancements": enhancements,
#         "width": width
#     }

#     data_dumped = {"parameters": json.dumps(data)}

#     response = requests.post(
#         'https://deep-image.ai/rest_api/process_result', 
#         headers=headers,
#         files={'image': file},
#         data=data_dumped
#     )

#     if response.status_code == 200:
#         response_json = response.json()
#         if response_json.get('status') == 'complete':
#             return response_json['result_url']
#         elif response_json['status'] in ['received', 'in_progress']:
#             while response_json['status'] == 'in_progress':
#                 response = requests.get(
#                     f'https://deep-image.ai/rest_api/result/{response_json["job"]}',
#                     headers=headers
#                 )
#                 response_json = response.json()
#                 time.sleep(1)
#             if response_json['status'] == 'complete':
#                 return response_json['result_url']
#     return None

# # Streamlit app
# def main():
#     st.title("Deep Image AI Image Processor")

#     # File uploader
#     uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

#     # Enhancements selection
#     enhancements = st.multiselect(
#         "Choose enhancements to apply", 
#         ["denoise", "deblur", "light", "color", "contrast"],
#         default=["denoise", "deblur", "light"]
#     )

#     # Image width input
#     width = st.number_input("Width of the output image", min_value=500, max_value=4000, value=2000)

#     if st.button("Process Image"):
#         if uploaded_file is not None:
#             # Process the image
#             result_url = process_image(uploaded_file, enhancements=enhancements, width=width)
#             if result_url:
#                 st.success("Image processed successfully!")
#                 st.image(result_url)
#             else:
#                 st.error("Failed to process image.")
#         else:
#             st.error("Please upload an image file.")

# if __name__ == "__main__":
#     main()
import time
import json
import requests
import streamlit as st

# Set your API key (Replace with your actual API key)
API_KEY = "de29e160-5bf0-11ef-a4dd-172f678d9c1e"

# Function to process the image using the Deep Image AI API
def process_image(file, enhancements=["denoise", "deblur", "light"], width=2000):
    headers = {
        'x-api-key': API_KEY,
    }
    data = {
        "enhancements": enhancements,
        "width": width
    }

    data_dumped = {"parameters": json.dumps(data)}

    response = requests.post(
        'https://deep-image.ai/rest_api/process_result', 
        headers=headers,
        files={'image': file},
        data=data_dumped
    )

    if response.status_code == 200:
        response_json = response.json()
        if response_json.get('status') == 'complete':
            return response_json['result_url']
        elif response_json['status'] in ['received', 'in_progress']:
            while response_json['status'] == 'in_progress':
                response = requests.get(
                    f'https://deep-image.ai/rest_api/result/{response_json["job"]}',
                    headers=headers
                )
                response_json = response.json()
                time.sleep(1)
            if response_json['status'] == 'complete':
                return response_json['result_url']
    return None

# Function to generate an image based on a text prompt
def generate_image_from_text(description, width=2048, height=1024):
    headers = {
        'x-api-key': API_KEY,
    }
    payload = {
        "width": width,
        "height": height,
        "background": {
            "generate": {
                "description": description
            }
        }
    }

    response = requests.post(
        'https://deep-image.ai/api/generate', 
        headers=headers, 
        data=json.dumps(payload)
    )

    if response.status_code == 200:
        response_json = response.json()
        if response_json.get('status') == 'complete':
            return response_json['result_url']
        elif response_json['status'] in ['received', 'in_progress']:
            while response_json['status'] == 'in_progress':
                response = requests.get(
                    f'https://deep-image.ai/rest_api/result/{response_json["job"]}',
                    headers=headers
                )
                response_json = response.json()
                time.sleep(1)
            if response_json['status'] == 'complete':
                return response_json['result_url']
    else:
        st.error(f"API request failed with status code {response.status_code}.")
    return None

# Streamlit app
def main():
    st.title("Deep Image AI Image Processor & Generator")

    # Tabs for different functionalities
    tab1, tab2 = st.tabs(["Enhance Image", "Generate Image"])

    # Image enhancement tab
    with tab1:
        st.header("Enhance Image")
        uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

        enhancements = st.multiselect(
            "Choose enhancements to apply", 
            ["denoise", "deblur", "light", "color", "contrast"],
            default=["denoise", "deblur", "light"]
        )

        width = st.number_input("Width of the output image", min_value=500, max_value=4000, value=2000)

        if st.button("Process Image"):
            if uploaded_file is not None:
                result_url = process_image(uploaded_file, enhancements=enhancements, width=width)
                if result_url:
                    st.success("Image processed successfully!")
                    st.image(result_url)
                else:
                    st.error("Failed to process image.")
            else:
                st.error("Please upload an image file.")

    # Image generation tab
    with tab2:
        st.header("Generate Image from Text")
        description = st.text_input("Enter a text description:")
        width = st.number_input("Width of the generated image", min_value=512, max_value=4096, value=2048)
        height = st.number_input("Height of the generated image", min_value=512, max_value=4096, value=1024)

        if st.button("Generate Image"):
            if description:
                result_url = generate_image_from_text(description, width, height)
                if result_url:
                    st.success("Image generated successfully!")
                    st.image(result_url)
                else:
                    st.error("Failed to generate image.")
            else:
                st.error("Please enter a description.")

if __name__ == "__main__":
    main()
