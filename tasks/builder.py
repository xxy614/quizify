import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from doc_processor import DocumentProcessor
from embed_client import EmbeddingClient
from chroma_creator import ChromaCollectionCreator


if __name__ == "__main__":
    st.header("Quizify")

    # Configuration for EmbeddingClient
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "sunny-inn-424902-g0",
        "location": "us-west1"
    }

    # 1) Initialize DocumentProcessor and Ingest Documents from Task 3
    processor = DocumentProcessor()
    
    # Display file uploader for document ingestion
    with st.form("Load Data to Chroma"):
        st.subheader("Quiz Builder")
        st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
        
        # Ingest documents
        processor.ingest_documents()

        # 2) Initialize the EmbeddingClient from Task 4 with embed config
        embed_client = EmbeddingClient(**embed_config)
        
        # 3) Initialize the ChromaCollectionCreator from Task 5
        chroma_creator = ChromaCollectionCreator(processor, embed_client)

        # 4) Use streamlit widgets to capture the user's input for the quiz topic and the desired number of questions
        topic_input = st.text_input("Topic for Generative Quiz", placeholder="Enter the topic of the document")
        questions = st.slider("Number of Questions", min_value=1, max_value=10, value=1)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            # 5) Use the create_chroma_collection() method to create a Chroma collection from the processed documents
            chroma_creator.create_chroma_collection()

            # Query Chroma collection
            document = chroma_creator.query_chroma_collection(topic_input)
            
            if document:
                st.success("Query Chroma for Topic, top Document:")
                st.write(document)
            else:
                st.error("No matching documents found for the query!", icon="🚨")