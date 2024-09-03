import streamlit as st
import requests
import PyPDF2
from PIL import Image
import docx
import io

# Function to simulate file upload by reading files from the disk
def programmatically_upload_files(file_paths):
    uploaded_files = []
    for file_path in file_paths:
        with open(file_path, "rb") as f:
            pdf_bytes = f.read()
            file_obj = io.BytesIO(pdf_bytes)
            file_obj.name = file_path  # Set the name attribute manually
            uploaded_files.append(file_obj)
    st.session_state.input_data['files'] = uploaded_files

# Function to extract text from PDFs
def extract_text_from_pdfs(pdf_files):
    combined_text = ""
    for pdf_file in pdf_files:
        try:
            reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
            combined_text += text + "\n"
        except Exception as e:
            st.error(f"Failed to read PDF file: {e}")
            return None
    return combined_text

# Function to extract text from DOCX files
def extract_text_from_docx(docx_files):
    combined_text = ""
    for docx_file in docx_files:
        try:
            doc = docx.Document(docx_file)
            text = "\n".join([para.text for para in doc.paragraphs])
            combined_text += text + "\n"
        except Exception as e:
            st.error(f"Failed to read DOCX file: {e}")
            return None
    return combined_text

# Function to process image files (e.g., PNG, JPG)
def process_images(image_files):
    image_texts = []
    for image_file in image_files:
        try:
            img = Image.open(image_file)
            st.image(img, caption=image_file.name)
            image_texts.append(f"Image file: {image_file.name}")
        except Exception as e:
            st.error(f"Failed to process image: {e}")
    return "\n".join(image_texts)

def call_api(data):
    api_url = "https://llama-1.onrender.com/history"
    
    # Construct the JSON payload
    payload = {
        "username": "siddharamsutar23@gmail.com",  # Ensure this is correct
        "prompt": data["content"]
    }
    
    # Define the headers
    headers = {
        "Content-Type": "application/json",  # Specify the content type
        "Accept": "application/json"           # Specify the expected response type
    }
    
    # Make the API request with headers
    response = requests.post(api_url, json=payload, headers=headers)
    
    # Check the response status
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"API request failed with status code {response.status_code}. Response: {response.text}")
        return None
    
# Function to display API response
def display_response(response):
    st.subheader("API Response")
    if isinstance(response, dict):
        for key, value in response.items():
            st.write(f"{key.capitalize()}: *{value}*")
    else:
        st.write(response)

# Main page
def main_page():
    st.title("Main Page")

    # Initialize session state
    if 'input_data' not in st.session_state:
        st.session_state.input_data = {'files': []}

    # Parse the JSON input
    input_json =st.query_params
    prompt = input_json.get("prompt", [""])[0]
    session_id = input_json.get("session_id", [""])[0]

    if prompt and session_id:
        # Programmatically upload files
        programmatically_upload_files([
            "C:/Users/HP/Downloads/Tele Law.pdf",
            "C:/Users/HP/Downloads/Vacancy.pdf"
        ])

        # Process the uploaded files
        if st.session_state.input_data['files']:
            files = st.session_state.input_data['files']
            combined_text = ""

            # Process PDF files
            pdf_files = [f for f in files if f.name.endswith('.pdf')]
            if pdf_files:
                pdf_text = extract_text_from_pdfs(pdf_files)
                if pdf_text:
                    combined_text += pdf_text

            # Process DOCX files
            docx_files = [f for f in files if f.name.endswith('.docx')]
            if docx_files:
                docx_text = extract_text_from_docx(docx_files)
                if docx_text:
                    combined_text += docx_text

            # Process Image files
            image_files = [f for f in files if f.name.lower().endswith(('.png', '.jpg', '.jpeg'))]
            if image_files:
                image_text = process_images(image_files)
                combined_text += image_text

            if combined_text:
                full_prompt = f"{prompt}\n\n{combined_text}"
                data = {"content": full_prompt}

                # Call the API with the combined content
                api_response = call_api(data)

                if api_response:
                    st.json(api_response)
            else:
                st.error("No valid content to process.")
        else:
            st.error("No files found to process.")
    else:
        st.error("Invalid JSON input. Please provide 'prompt' and 'session_id'.")

# Run the app
if __name__ == "__main__":
    main_page()