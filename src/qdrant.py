from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from dotenv import load_dotenv
import os


load_dotenv(override=True)

class Qdrant():
    def __init__(self) -> None:
        self.client = QdrantClient(url=os.environ.get("QDRANT_URL", "http://localhost:6333"))

    def create_collection(self, collection_name) -> None:
        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=4, distance=Distance.DOT),
        )

