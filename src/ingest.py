import os

from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_qdrant import QdrantVectorStore

from ai import get_embedding_model


def ingest_data(file_path, collection_name):
    loader = CSVLoader(file_path=file_path)
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    split_docs = text_splitter.split_documents(docs)


    embedding_model = get_embedding_model()

    vector_store = QdrantVectorStore.from_documents(
        documents=split_docs,
        url=os.environ.get("QDRANT_URL", "http://localhost:6333"),
        collection_name=collection_name,
        embedding=embedding_model,
    )

