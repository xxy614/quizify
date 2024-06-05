import streamlit as st
import os
import sys
import json
sys.path.append(os.path.abspath('../../'))
from doc_processor import DocumentProcessor
from embed_client import EmbeddingClient
from chroma_creator import ChromaCollectionCreator
from q_generator import QuizGenerator

class QuizManager:
    def __init__(self, questions: list):
        self.questions = questions
        self.total_questions = len(questions)
    
    def get_question_at_index(self, index: int):
        valid_index = index % self.total_questions
        return self.questions[valid_index]
    
    def next_question_index(self, direction=1):
        current_index = st.session_state.get("question_index", 0)
        new_index = (current_index + direction) % self.total_questions
        st.session_state["question_index"] = new_index

# Test Generating the Quiz
if __name__ == "__main__":
    
    embed_config = {
        "model_name": "textembedding-gecko@003",
        "project": "sunny-inn-424902-g0",
        "location": "us-central1"
    }
    
    screen = st.empty()
    with screen.container():
        st.header("Quiz Builder")
        processor = DocumentProcessor()
        processor.ingest_documents()
    
        embed_client = EmbeddingClient(**embed_config) 
    
        chroma_creator = ChromaCollectionCreator(processor, embed_client)
    
        question_bank = None
    
        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate!")
            
            topic_input = st.text_input("Topic for Generative Quiz", placeholder="Enter the topic of the document")
            questions = st.slider("Number of Questions", min_value=1, max_value=10, value=1)
            
            submitted = st.form_submit_button("Submit")
            if submitted:
                chroma_creator.create_chroma_collection()
                st.write(topic_input)
                
                # Test the Quiz Generator
                generator = QuizGenerator(topic_input, questions, chroma_creator)
                question_bank = generator.generate_quiz()

    if question_bank:
        screen.empty()
        with st.container():
            st.header("Generated Quiz Question: ")
            
            quiz_manager = QuizManager(question_bank)
            if "question_index" not in st.session_state:
                st.session_state["question_index"] = 0
            
            index_question = quiz_manager.get_question_at_index(st.session_state["question_index"])
            
            choices = []
            for choice in index_question['choices']:
                key = choice['key']
                value = choice['value']
                choices.append(f"{key}) {value}")
            
            st.write(index_question['question'])
            answer = st.radio('Choose the correct answer', choices)
            
            submitted_answer = st.button("Submit Answer")
            if submitted_answer:
                correct_answer_key = index_question['answer']
                if answer.startswith(correct_answer_key):
                    st.success("Correct!")
                else:
                    st.error("Incorrect!")
            
            if st.button("Next Question"):
                quiz_manager.next_question_index(1)
                st.experimental_rerun()
            
            if st.button("Previous Question"):
                quiz_manager.next_question_index(-1)
                st.experimental_rerun()
