# bot/config.py
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
def load_model(model_name="gemini-2.0-flash"):
    """Inicializa o modelo Gemini."""
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    return ChatGoogleGenerativeAI(model=model_name, google_api_key=GOOGLE_API_KEY)
