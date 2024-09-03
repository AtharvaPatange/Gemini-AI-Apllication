import streamlit as st
import google.generativeai as genai
from transformers import pipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from sklearn.linear_model import LogisticRegression
from dotenv import load_dotenv
from PyPDF2 import PdfReader

load_dotenv()

# Configure your API keys
genai.configure(api_key="YOUR_API_KEY_HERE")  # Replace with your API key
google_api_key = "YOUR_API_KEY_HERE"  # Replace with your API key

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        except Exception as e:
            st.error(f"Error reading PDF: {str(e)}")
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local("faiss_index")
    except Exception as e:
        st.error(f"Error creating embeddings: {str(e)}")
        raise

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. If the answer is not in the context, say, "answer is not available in the context".
    
    Context:\n{context}\n
    Question:\n{question}\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question, case_features):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(user_question)

        chain = get_conversational_chain()
        response = chain(
            {"input_documents": docs, "question": user_question},
            return_only_outputs=True
        )

        # Predict outcome using the output prediction model
        outcome_prediction = predict_outcome(case_features)

        # Combine the response from Gemini API and the outcome prediction
        final_response = f"{response['output_text']}\n\nBased on the case features, the predicted outcome is: {outcome_prediction}"

        st.write("Reply: ", final_response)
    except Exception as e:
        st.error(f"Error during user input processing: {str(e)}")

def predict_outcome(case_features):
    model = LogisticRegression()
    model.fit(X_train, y_train)  # Assuming you have pre-trained the model
    prediction = model.predict([case_features])
    return prediction[0]

def main_page():
    st.header("Main Page: Chat with PDF using Gemini💁")
    
    user_question = st.text_input("Ask a Question from the PDF Files")
    case_features = st.text_input("Enter case features (e.g., judge, case type, legal arguments)")
    
    if user_question and case_features:
        user_input(user_question, case_features.split(","))

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

def settings_page():
    st.header("Settings Page")
    st.write("Here you can adjust your settings.")

def about_page():
    st.header("About Page")
    st.write("This app allows you to chat with PDF files using the Gemini AI model and predict case outcomes.")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Main Page", "Settings", "About"])

    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: black;
        }
        [data-testid="stSidebar"] * {
            color: white;
        }
        .stFileUpload div[role="button"] {
            background-color: #FFF8E1;
            color: black;
            border: 1px solid #DDD;
            border-radius: 4px;
        }
        .stFileUpload .stDropzone {
            background-color: #FFF8E1;
            border: 1px dashed #DDD;
            border-radius: 4px;
        }
        .stButton > button {
            background-color: #FFF8E1;
            color: black;
            border: 1px solid #DDD;
            border-radius: 4px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if page == "Main Page":
        main_page()
    elif page == "Settings":
        settings_page()
    elif page == "About":
        about_page()

if __name__ == "__main__":
    main()