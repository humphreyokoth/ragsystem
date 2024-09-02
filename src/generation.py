from transformers import pipeline
from src.config import MODEL_NAME, HUGGINGFACE_API_KEY
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

generator = pipeline("text-generation", model=MODEL_NAME, api_key=HUGGINGFACE_API_KEY)


def generate_response(retrieved_docs: List[Dict]) -> str:
    try:
        context = " ".join([doc["_source"]["text"] for doc in retrieved_docs])
        response = generator(context, max_length=50, num_return_sequences=1)
        return response[0]["generated_text"]
    except Exception as e:
        logger.error(f"Error generating response: {str(e)}")
        raise
