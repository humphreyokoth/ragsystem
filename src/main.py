import logging
from ragsystem.config import MODEL_NAME, HUGGINGFACE_API_KEY
from ragsystem.data_extraction import extract_text_from_google_docs
from ragsystem.indexing import index_text
from ragsystem.retrieval import retrieve_documents
from ragsystem.generation import generate_response

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    try:
        # Extract text from Google Docs
        logger.info("Extracting text from Google Docs...")
        text_content = extract_text_from_google_docs()

        # Index the extracted text
        logger.info("Indexing extracted text...")
        index_text(text_content)

        # Retrieve documents based on a query
        query = "Sample query"  # Replace with an actual query
        logger.info(f"Retrieving documents for query: {query}")
        retrieved_docs = retrieve_documents(query)

        # Generate a response
        logger.info("Generating response...")
        response = generate_response(retrieved_docs)

        print(f"Generated response: {response}")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
