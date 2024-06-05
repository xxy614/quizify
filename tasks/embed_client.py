from langchain_google_vertexai import VertexAIEmbeddings
import os
import json

class EmbeddingClient:
    """
    Task: Initialize the EmbeddingClient class to connect to Google Cloud's VertexAI for text embeddings.
    """

    def __init__(self, model_name, project, location):
        # Set environment variable for GOOGLE_APPLICATION_CREDENTIALS
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "D:\\xinyu\\quizify\\mission-quizify\\authentication.json"

        # Validate the JSON content
        config_path = os.environ['GOOGLE_APPLICATION_CREDENTIALS']
        with open(config_path, 'r') as f:
            try:
                data = json.load(f)
                print("JSON content is valid.")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return

        # Initialize the VertexAIEmbeddings client with the given parameters
        self.client = VertexAIEmbeddings(
            model=model_name,
            project=project,
            location=location
        )

    def embed_query(self, query):
        """
        Uses the embedding client to retrieve embeddings for the given query.
        """
        vectors = self.client.embed_query(query)
        return vectors

    def embed_documents(self, documents):
        """
        Retrieve embeddings for multiple documents.
        """
        return self.client.embed_documents(documents)

if __name__ == "__main__":
    model_name = "textembedding-gecko@003"
    project = "sunny-inn-424902-g0"
    location = "us-central1"

    embedding_client = EmbeddingClient(model_name, project, location)
    vectors = embedding_client.embed_query("Hello World!")
    if vectors:
        print(vectors)
        print("Successfully used the embedding client!")
