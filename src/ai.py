from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv


load_dotenv(override=True)

def get_embedding_model():
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.environ.get("GEMINI_API_KEY")
    )

    return embedding_model
