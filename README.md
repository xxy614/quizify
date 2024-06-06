# Quizify Project

## Overview

Quizify is an interactive quiz generation and management application built using Streamlit. It leverages machine learning models and document processing techniques to generate quizzes based on uploaded PDF documents. The project integrates various components including document processing, embedding using Google VertexAI, and a custom-built quiz management system.

## Project Structure

```plaintext
mission-quizify/
├── tasks/
│   ├── doc_processor.py
│   ├── embed_client.py
│   ├── chroma_creator.py
│   ├── builder.py
│   ├── q_generator.py
│   ├── question_generator.py
│   ├── manager.py
│   └── application.py
├── requirements.txt
└── authentication.json
```

## File and Task Descriptions

- **docu_processor.py**
  - Handles the processing and splitting of uploaded PDF documents.

- **embed_client.py**
  - Initializes and configures the embedding client for Google Cloud's VertexAI, generating text embeddings.

- **chroma_creator.py**
  - Creates Chroma collections from processed documents using the embedding client and supports querying.

- **qbuilder.py**
  - Creates an interactive Quiz Builder application using Streamlit, allowing users to upload documents, specify quiz topics, and generate quiz questions.

- **q_generator.py**
  - Initializes and configures the LLM for generating quiz questions based on specific topics.

- **question_generator.py**
  - Generates a series of unique quiz questions based on a specified topic and number of questions.

- **manager.py**
  - Manages and displays quiz questions, supporting navigation between questions.

- **application.py**
  - Builds the complete quiz application using Streamlit, including document processing, embedding generation, Chroma collection creation, quiz question generation, and quiz management.


## Requirements

- Python 3.8 or higher
- Streamlit
- LangChain
- Google VertexAI
- Chroma

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/quizify.git
    cd quizify
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv myenv
    ```
    On Mac\Linux
    ```bash
    source myenv/bin/activate  
    ```
    On Windows
    ```bash
    myenv\Scripts\activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Google VertexAI credentials:
    Ensure you have your `authentication.json` file and set the environment variable:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="path/to/authentication.json"
    ```

## Running the Application

To run the application, navigate to the respective task folder and execute the Streamlit application. For example, to run application.py:
```bash
cd mission-quizify/tasks
streamlit run application.py
```

## Task Details

- **Task 3: Document Processing**
- File: `tasks/doc_processor.py`
- Function: Processes uploaded PDF documents, including parsing and extracting pages.

- **Task 4: Embedding Client**
- File: `tasks/embed_client.py`
- Function: Connects to Google Cloud's VertexAI to generate text embeddings.

- **Task 5: Chroma Collection Creation**
- File: `tasks/chroma_creator.py`
- Function: Creates a Chroma collection from processed documents for subsequent querying and processing.

- **Task 6: Quiz Builder Integration**
- File: `tasks/builder.py`
- Function: Creates an interactive application using Streamlit to generate quiz questions based on uploaded documents. This task integrates DocumentProcessor, EmbeddingClient, and ChromaCollectionCreator.

- **Task 7: Quiz Question Generation**
- File: `tasks/question_generator.py`
- Function: Generates quiz questions using an LLM and vector store.

- **Task 8: Quiz Generation**
- File: `tasks/q_generator.py`
- Function: Generates a list of unique quiz questions based on a specified topic and number of questions.

- **Task 9: Quiz Management**
- File: `tasks/manager.py`
- Function: Manages quiz questions, allowing navigation through questions and answer submission using Streamlit.

- **Task 10: Session State Handling and Quiz Navigation**
- File: `tasks/application.py`
- Adds session state handling in Streamlit, initializes and displays the quiz, and provides navigation through quiz questions.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
