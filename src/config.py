import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_DOCS_DOCUMENT_ID = os.getenv('GOOGLE_DOCS_DOCUMENT_ID')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
ELASTICSEARCH_CLOUD_ID = os.getenv('ELASTICSEARCH_CLOUD_ID')
ELASTICSEARCH_API_KEY = os.getenv('ELASTICSEARCH_API_KEY')
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY')

INDEX_NAME = "documents"
MODEL_NAME = "facebook/blenderbot-400M-distill"