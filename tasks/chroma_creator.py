import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from doc_processor import DocumentProcessor
from embed_client import EmbeddingClient


# Import Task libraries
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

class SimpleDocument:
    def __init__(self, text, metadata={}):
        self.page_content = text
        self.metadata = metadata


class ChromaCollectionCreator:
    def __init__(self, processor, embed_model):
        self.processor = processor
        self.embed_model = embed_model
        self.db = None
    
    def create_chroma_collection(self):
        if len(self.processor.pages) == 0:
            st.error("No documents found!", icon="🚨")
            return
        separator = " "
        chunk_size = 100
        chunk_overlap = 20
        text_splitter = CharacterTextSplitter(separator=separator, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        texts = text_splitter.split_documents([Document(page_content=str(page)) for page in self.processor.pages])
        if texts:
            st.success(f"Successfully split pages to {len(texts)} documents!", icon="✅")
        self.db = Chroma(
            collection_name="DocumentCollection",
            embedding_function=self.embed_model
        )
        self.db.add_documents(texts)
        if self.db:
            st.success("Successfully created Chroma Collection!", icon="✅")
        else:
            st.error("Failed to create Chroma Collection!", icon="🚨")
    
    def query_chroma_collection(self, query):
        if self.db:
            docs = self.db.similarity_search(query)
            if docs:
                return docs
            else:
                st.error("No matching documents found!", icon="🚨")
        else:
            st.error("Chroma Collection has not been created!", icon="🚨")
        return None


if __name__ == "__main__":
    processor = DocumentProcessor()
    processor.ingest_documents()
    
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "sunny-inn-424902-g0",
        "location": "us-west1"
    }
    
    embed_client = EmbeddingClient(**embed_config)
    print(type(embed_client))
    
    chroma_creator = ChromaCollectionCreator(processor, embed_client)
    
    with st.form("Load Data to Chroma"):
        st.write("Select PDFs for Ingestion, then click Submit")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            chroma_creator.create_chroma_collection()