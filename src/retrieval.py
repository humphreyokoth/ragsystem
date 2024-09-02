from elasticsearch import Elasticsearch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.config import ELASTICSEARCH_CLOUD_ID, ELASTICSEARCH_API_KEY, INDEX_NAME
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

es = Elasticsearch(cloud_id=ELASTICSEARCH_CLOUD_ID, api_key=ELASTICSEARCH_API_KEY)


def retrieve_documents(query: str, index_name: str = INDEX_NAME) -> List[Dict]:
    try:
        response = es.search(index=index_name, query={"match_all": {}}, size=1000)
        documents = [hit["_source"]["text"] for hit in response["hits"]["hits"]]

        vectorizer = TfidfVectorizer().fit_transform(documents + [query])
        vectors = vectorizer.toarray()
        query_vector = vectors[-1].reshape(1, -1)
        document_vectors = vectors[:-1]

        similarities = cosine_similarity(query_vector, document_vectors).flatten()

        ranked_docs = [
            {"_source": {"text": doc}}
            for doc, sim in sorted(
                zip(documents, similarities), key=lambda x: x[1], reverse=True
            )
        ]

        return ranked_docs
    except Exception as e:
        logger.error(f"Error retrieving documents: {str(e)}")
        raise
