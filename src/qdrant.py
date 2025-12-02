from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
from ai import get_embedding_model
import os


load_dotenv(override=True)

class Qdrant():
    def __init__(self) -> None:
        self.client = QdrantClient(url=os.environ.get("QDRANT_URL", "http://localhost:6333"))

    def create_collection(self, collection_name, documents) -> None:
        embedding_model = get_embedding_model()

        vector_store = QdrantVectorStore.from_documents(
            documents=documents,
            url=os.environ.get("QDRANT_URL", "http://localhost:6333"),
            collection_name=collection_name,
            embedding=embedding_model,
        )

