from elasticsearch import Elasticsearch
from src.config import ELASTICSEARCH_CLOUD_ID, ELASTICSEARCH_API_KEY, INDEX_NAME
import logging

logger = logging.getLogger(__name__)

es = Elasticsearch(cloud_id=ELASTICSEARCH_CLOUD_ID, api_key=ELASTICSEARCH_API_KEY)


def index_text(text: str, index_name: str = INDEX_NAME) -> None:
    try:

        if not es.indices.exists(index=index_name):
            es.indices.create(index=index_name)

        es.index(index=index_name, document={"text": text})
        logger.info(f"Text indexed successfully in {index_name}")
    except Exception as e:
        logger.error(f"Error indexing text: {str(e)}")
        raise
