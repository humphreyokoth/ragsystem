import requests
import logging
from src.config import GOOGLE_DOCS_DOCUMENT_ID, GOOGLE_API_KEY

logger = logging.getLogger(__name__)


def extract_text_from_google_docs():
    try:
        url = f"https://docs.googleapis.com/v1/documents/{GOOGLE_DOCS_DOCUMENT_ID}?key={GOOGLE_API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        doc = response.json()

        full_text = ""
        for content in doc.get("body", {}).get("content", []):
            if "paragraph" in content:
                for element in content["paragraph"].get("elements", []):
                    if "textRun" in element:
                        full_text += element["textRun"].get("content", "")

        return full_text
    except requests.RequestException as e:
        logger.error(f"Error extracting text from Google Docs: {str(e)}")
        raise
