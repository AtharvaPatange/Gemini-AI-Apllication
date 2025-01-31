# import streamlit as st
# from PyPDF2 import PdfReader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# import google.generativeai as genai
# from langchain.vectorstores import FAISS
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains.question_answering import load_qa_chain
# from langchain.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your API key from environment
# google_api_key = "YOUR_API_KEY_HERE"  # Replace with your API key from environment

# def get_pdf_text(pdf_docs):
#     text = ""
#     for pdf in pdf_docs:
#         try:
#             pdf_reader = PdfReader(pdf)
#             for page in pdf_reader.pages:
#                 text += page.extract_text()
#         except Exception as e:
#             st.error(f"Error reading PDF: {str(e)}")
#     return text

# def get_text_chunks(text):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
#     chunks = text_splitter.split_text(text)
#     return chunks

# def get_vector_store(text_chunks):
#     try:
#         embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#         vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
#         vector_store.save_local("faiss_index")
#     except Exception as e:
#         st.error(f"Error creating embeddings: {str(e)}")
#         raise

# def get_conversational_chain():
#     prompt_template = """
#     Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
#     provided context just say, "answer is not available in the context", if something related  to input keyword is found tell all about it \n\n
#     Context:\n {context}?\n
#     Question: \n{question}\n

#     Answer:
#     """

#     model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
#     prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
#     chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

#     return chain

# def user_input(user_question):
#     try:
#         embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#         new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
#         docs = new_db.similarity_search(user_question)

#         chain = get_conversational_chain()
#         response = chain(
#             {"input_documents": docs, "question": user_question},
#             return_only_outputs=True
#         )

#         st.write("Reply: ", response["output_text"])
#     except Exception as e:
#         st.error(f"Error during user input processing: {str(e)}")


# # Page 1: Main page
# def main_page():
#     st.header("Main Page: Chat with PDF using Gemini💁")
    
#     user_question = st.text_input("Ask a Question from the PDF Files")
    
#     if user_question:
#         user_input(user_question)  # Assuming user_input is already defined elsewhere

#     with st.sidebar:
#         st.title("Menu:")
#         pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
#         if st.button("Submit & Process"):
#             with st.spinner("Processing..."):
#                 raw_text = get_pdf_text(pdf_docs)  # Assuming get_pdf_text is already defined elsewhere
#                 text_chunks = get_text_chunks(raw_text)  # Assuming get_text_chunks is already defined elsewhere
#                 get_vector_store(text_chunks)  # Assuming get_vector_store is already defined elsewhere
#                 st.success("Done")


# # Page 2: Settings
# def settings_page():
#     st.header("Settings Page")
#     st.write("Here you can adjust your settings.")
#     # Add your settings options here

# # Page 3: About
# def about_page():
#     st.header("About Page")
#     st.write("This app allows you to chat with PDF files using the Gemini AI model.")
#     # Add more about information here

# # Main app
# def main():
#     # Sidebar navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", ["Main Page", "Settings", "About"])

#     # Apply custom CSS styles (Optional, if you want the styles on all pages)
#     st.markdown(
#         """
#         <style>
#         /* Sidebar background */
#         [data-testid="stSidebar"] {
#             background-color: black;
#         }
#         /* Sidebar text color */
#         [data-testid="stSidebar"] * {
#             color: white;
#         }
#         /* Upload button container background */
#         .stFileUpload div[role="button"] {
#             background-color: #FFF8E1; /* Cream yellow */
#             color: black;
#             border: 1px solid #DDD;
#             border-radius: 4px;
#         }
#         /* Drag and drop area background */
#         .stFileUpload .stDropzone {
#             background-color: #FFF8E1;
#             border: 1px dashed #DDD;
#             border-radius: 4px;
#         }
#         /* Submit & Process button background */
#         .stButton > button {
#             background-color: #FFF8E1;
#             color: black;
#             border: 1px solid #DDD;
#             border-radius: 4px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # Render the selected page
#     if page == "Main Page":
#         main_page()
#     elif page == "Settings":
#         settings_page()
#     elif page == "About":
#         about_page()

# if __name__ == "__main__":
#     main()
# # def main():
# #     st.markdown(
# #     """
# #     <style>
# #     /* Sidebar background */
# #     [data-testid="stSidebar"] {
# #         background-color: black;
# #     }
# #     /* Sidebar text color */
# #     [data-testid="stSidebar"] * {
# #         color: black;
# #     }
# #     /* Upload button container background */
# #     .stFileUpload div[role="button"] {
# #         background-color: #FFF8E1; /* Cream yellow */
# #         color: black;
# #         border: 1px solid #DDD; /* Optional: add a border to make it stand out */
# #         border-radius: 4px; /* Optional: rounded corners */
# #     }
# #     /* Drag and drop area background */
# #     .stFileUpload .stDropzone {
# #         background-color: #FFF8E1; /* Cream yellow */
# #         border: 1px dashed #DDD; /* Optional: add a dashed border */
# #         border-radius: 4px; /* Optional: rounded corners */
# #     }
# #     /* Submit & Process button background */
# #     .stButton > button {
# #         background-color: #FFF8E1; /* Cream yellow */
# #         color: black;
# #         border: 1px solid #DDD; /* Optional: add a border to make it stand out */
# #         border-radius: 4px; /* Optional: rounded corners */
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )

# #     st.header("Chat with PDF using Gemini💁")

# #     user_question = st.text_input("Ask a Question from the PDF Files")

# #     if user_question:
# #         user_input(user_question)

# #     with st.sidebar:
# #         st.title("Menu:")
# #         pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
# #         if st.button("Submit & Process"):
# #             with st.spinner("Processing..."):
# #                 raw_text = get_pdf_text(pdf_docs)
# #                 text_chunks = get_text_chunks(raw_text)
# #                 get_vector_store(text_chunks)
# #                 st.success("Done")

# # if __name__ == "__main__":
# #     main()


# import streamlit as st
# from PyPDF2 import PdfReader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# import os
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# import google.generativeai as genai
# from langchain.vectorstores import FAISS
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains.question_answering import load_qa_chain
# from langchain.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()


# genai.configure(api_key="AIzaSyAb_szzFcil2GC2UJHq_ooE6bb-Z9fkA3o")
# google_api_key="AIzaSyAb_szzFcil2GC2UJHq_ooE6bb-Z9fkA3o"






# def get_pdf_text(pdf_docs):
#     text=""
#     for pdf in pdf_docs:
#         pdf_reader= PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text+= page.extract_text()
#     return  text



# def get_text_chunks(text):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
#     chunks = text_splitter.split_text(text)
#     return chunks


# # def get_vector_store(text_chunks):
# #     embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
# #     vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
# #     vector_store.save_local("faiss_index")
# def get_vector_store(text_chunks):
#     try:
#         embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#         vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
#         vector_store.save_local("faiss_index")
#     except Exception as e:
#         st.error(f"Error creating embeddings: {str(e)}")
#         raise


# def get_conversational_chain():

#     prompt_template = """
#     Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
#     provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
#     Context:\n {context}?\n
#     Question: \n{question}\n

#     Answer:
#     """

#     model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

#     prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
#     chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

#     return chain



# def user_input(user_question):
#     embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
#     new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
#     docs = new_db.similarity_search(user_question)

#     chain = get_conversational_chain()

#     response = chain(
#         {"input_documents": docs, "question": user_question},
#         return_only_outputs=True
#     )

#     print(response)
#     st.write("Reply: ", response["output_text"])





# def main():
#     st.set_page_config("Chat PDF")
#     st.header("Department Of Justice")

#     user_question = st.text_input("Ask a Question from the PDF Files")

#     if user_question:
#         user_input(user_question)

#     with st.sidebar:
#         st.title("Menu:")
#         pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
#         if st.button("Submit & Process"):
#             with st.spinner("Processing..."):
#                 raw_text = get_pdf_text(pdf_docs)
#                 text_chunks = get_text_chunks(raw_text)
#                 get_vector_store(text_chunks)
#                 st.success("Done")



# if __name__ == "__main__":
#     main()

#######################################\

# import os
# import json
# import requests
# from io import BytesIO
# from flask import Flask, request, jsonify
# from PyPDF2 import PdfReader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains.question_answering import load_qa_chain
# from langchain.prompts import PromptTemplate
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# app = Flask(__name__)

# # Function to get text from a single PDF URL
# def get_pdf_text_from_url(pdf_url):
#     try:
#         response = requests.get(pdf_url)
#         response.raise_for_status()
#         pdf_file = BytesIO(response.content)
#         pdf_reader = PdfReader(pdf_file)
#         text = ""
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#         return text
#     except Exception as e:
#         print(f"Error reading PDF from URL {pdf_url}: {str(e)}")
#         return None

# def get_text_chunks(text):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
#     chunks = text_splitter.split_text(text)
#     return chunks

# def create_vector_store(text_chunks):
#     try:
#         embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#         vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
#         vector_store.save_local("faiss_index")
#     except Exception as e:
#         raise Exception(f"Error creating embeddings: {str(e)}")

# def get_conversational_chain():
#     prompt_template = """
   
#     \n\n
#     Context:\n{context}\n
#     Question:\n{question}\n
#     Answer:
#     """
#     model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
#     prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
#     chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
#     return chain

# @app.route('/process', methods=['POST'])
# def process_request():
#     try:
#         # Parse JSON input
#         input_data = request.get_json()
#         prompt = input_data.get("prompt")
#         pdf_url = input_data.get("url")

#         if not prompt or not pdf_url:
#             return jsonify({"error": "Prompt or URL is missing in the input."}), 400

#         # Extract text from PDF
#         raw_text = get_pdf_text_from_url(pdf_url)
#         if not raw_text:
#             return jsonify({"error": "Failed to extract text from PDF."}), 500

#         # Process text
#         text_chunks = get_text_chunks(raw_text)
#         create_vector_store(text_chunks)

#         # Load vector store and search for relevant documents
#         embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#         vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
#         docs = vector_store.similarity_search(prompt)

#         # Generate response using conversational chain
#         chain = get_conversational_chain()
#         response = chain({"input_documents": docs, "question": prompt}, return_only_outputs=True)

#         return jsonify({"response": response["output_text"]}), 200

#     except Exception as e:
#         return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


#############################
import os
import requests
from io import BytesIO
from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from flask_cors import CORS
# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Global variables to store vector store and embeddings
vector_store = None
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Function to get text from a single PDF URL
def get_pdf_text_from_url(pdf_url):
    try:
        response = requests.get(pdf_url)
        response.raise_for_status()
        pdf_file = BytesIO(response.content)
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading PDF from URL {pdf_url}: {str(e)}")
        return None

# Function to split text into chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create and save vector store once
def create_vector_store(text_chunks):
    global vector_store
    try:
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
    except Exception as e:
        raise Exception(f"Error creating vector store: {str(e)}")

# Function to load vector store if it exists
def load_vector_store():
    global vector_store
    if vector_store is None:
        try:
            vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        except Exception as e:
            raise Exception(f"Error loading vector store: {str(e)}")

# Function to get conversational chain
def get_conversational_chain():
    prompt_template = """
    You are provided with data from the Department of Justice in India. Try to answer the input question, including any relevant information.
    \n\n
    Context:\n{context}\n
    Question:\n{question}\n
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.8)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

# Route to handle requests
@app.route('/process', methods=['POST'])
def process_request():
    try:
        # Load vector store if not already loaded
        load_vector_store()

        # Parse JSON input
        input_data = request.get_json()
        prompt = input_data.get("prompt")

        if not prompt:
            return jsonify({"error": "Prompt is missing in the input."}), 400

        # Perform similarity search using the vector store
        docs = vector_store.similarity_search(prompt)

        # Generate response using conversational chain
        chain = get_conversational_chain()
        response = chain({"input_documents": docs, "question": prompt}, return_only_outputs=True)

        return jsonify({"response": response["output_text"]}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Function to initialize the vector store at application startup
def initialize_vector_store():
    # Define your list of PDF URLs here
    PDF_URLS = [
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/ALAHABAD%20High%20Court.pdf?alt=media&token=167623fa-bd50-451a-999c-937403109289",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/ANDHRA.pdf?alt=media&token=cae63b52-1a58-403d-a082-ed31cf0f5f05",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/BOMBAY.pdf?alt=media&token=67970fe5-10ff-46e2-954d-6a07b9d30da0",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/FAST%20Track%20Special%20Court.pdf?alt=media&token=df061683-e8fc-474e-a1da-e9ccfb2ca326",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/High%20Court%20Vacancy.pdf?alt=media&token=5e24ffbd-ccfe-4160-b875-a4893974422e",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/Higher%20Higher%20Judges.pdf?alt=media&token=d34cf137-0bb9-4b2a-bf3e-9c9dfcce3db9",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/JUDGES.pdf?alt=media&token=bd26d405-c58d-41e0-b6b6-2155d542dc32",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/Supreme%20Court%20Vacancy.pdf?alt=media&token=60926839-6614-43ed-9a6d-c5483d7d884d",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/Tele%20Law.pdf?alt=media&token=d71883a9-5b77-4fae-8723-55ba29c97e1e",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/Vacancy.pdf?alt=media&token=49f7d48b-c258-44d4-b6fd-f5ba447576f7",
        "https://firebasestorage.googleapis.com/v0/b/dojweb-de6e2.appspot.com/o/alldataofdojinpdf.pdf?alt=media&token=272e4f0f-35ce-4bac-afff-e9c86f7f43dd"

    ]

    # Extract text from all PDFs and process it once
    raw_text = ""
    for url in PDF_URLS:
        pdf_text = get_pdf_text_from_url(url)
        if pdf_text:
            raw_text += pdf_text + "\n"
    
    if raw_text:
        # Process text into chunks
        text_chunks = get_text_chunks(raw_text)

        # Create and save the vector store
        create_vector_store(text_chunks)

if __name__ == "__main__":
    # Initialize vector store before the app runs
    initialize_vector_store()
    app.run(host='0.0.0.0', port=5000)

# import streamlit as st
# import time
# from PyPDF2 import PdfReader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# import google.generativeai as genai
# from langchain.vectorstores import FAISS
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.chains.question_answering import load_qa_chain
# from langchain.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your API key from environment
# google_api_key = "YOUR_API_KEY_HERE"  # Replace with your API key from environment

# # Function to show the splash screen with the Department of Justice logo
# def show_splash_screen():
#     st.markdown(
#         """
#         <style>
#         .splash-screen {
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             height: 100vh;
#             background-color: #000; /* Black background */
#         }
#         .splash-screen img {
#             max-width: 300px;
#             max-height: 300px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         """
#         <div class="splash-screen">
#             <img src="https://d3fp5tyfm1gdbn.cloudfront.net/2022/Sep/02/1662116974_DOJ-Logo.png">
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
#     time.sleep(3)  # Display the splash screen for 3 seconds

# # Function to get PDF text
# def get_pdf_text(pdf_docs):
#     text = ""
#     for pdf in pdf_docs:
#         try:
#             pdf_reader = PdfReader(pdf)
#             for page in pdf_reader.pages:
#                 text += page.extract_text()
#         except Exception as e:
#             st.error(f"Error reading PDF: {str(e)}")
#     return text

# # Function to get text chunks
# def get_text_chunks(text):
#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
#     chunks = text_splitter.split_text(text)
#     return chunks

# # Function to get vector store
# def get_vector_store(text_chunks):
#     try:
#         embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#         vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
#         vector_store.save_local("faiss_index")
#     except Exception as e:
#         st.error(f"Error creating embeddings: {str(e)}")
#         raise

# # Function to get conversational chain
# def get_conversational_chain():
#     prompt_template = """
#     Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
#     provided context just say, "answer is not available in the context", if something related  to input keyword is found tell all about it \n\n
#     Context:\n {context}?\n
#     Question: \n{question}\n

#     Answer:
#     """

#     model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
#     prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
#     chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

#     return chain

# # Function to process user input and display conversation history
# def user_input(user_question, history):
#     try:
#         embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
#         new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
#         docs = new_db.similarity_search(user_question)

#         chain = get_conversational_chain()
#         response = chain(
#             {"input_documents": docs, "question": user_question},
#             return_only_outputs=True
#         )

#         history.append((user_question, response["output_text"]))
#         for query, reply in history:
#             st.write(f"**You:** {query}")
#             st.write(f"**Bot:** {reply}")
#     except Exception as e:
#         st.error(f"Error during user input processing: {str(e)}")


# # Page 1: Main page
# def main_page():
#     st.header("Main Page: Chat with PDF using Gemini💁")
    
#     user_question = st.text_input("Ask a Question from the PDF Files")
    
#     if user_question:
#         user_input(user_question, st.session_state['history'])

#     with st.sidebar:
#         st.title("Menu:")
#         pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
#         if st.button("Submit & Process"):
#             with st.spinner("Processing..."):
#                 raw_text = get_pdf_text(pdf_docs)  # Assuming get_pdf_text is already defined elsewhere
#                 text_chunks = get_text_chunks(raw_text)  # Assuming get_text_chunks is already defined elsewhere
#                 get_vector_store(text_chunks)  # Assuming get_vector_store is already defined elsewhere
#                 st.success("Done")

# # Page 2: Settings
# def settings_page():
#     st.header("Settings Page")
#     st.write("Here you can adjust your settings.")

# # Page 3: About
# def about_page():
#     st.header("About Page")
#     st.write("This app allows you to chat with PDF files using the Gemini AI model.")

# # Main app
# def main():
#     # Show splash screen on first load
#     if 'first_load' not in st.session_state:
#         st.session_state['first_load'] = True
#         st.session_state['history'] = []
#         show_splash_screen()

#     # Sidebar navigation
#     st.sidebar.title("Navigation")
#     page = st.sidebar.radio("Go to", ["Main Page", "Settings", "About"])

#     # Render the selected page
#     if page == "Main Page":
#         main_page()
#     elif page == "Settings":
#         settings_page()
#     elif page == "About":
#         about_page()

# if __name__ == "__main__":
#     main()
