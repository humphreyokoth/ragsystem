import unittest
from src.retrieval import retrieve_documents


class TestRetrieval(unittest.TestCase):
    def test_retrieve_documents(self):
        query = "test"
        retrieved_docs = retrieve_documents(query, index_name="test_index")
        self.assertIsNotNone(retrieved_docs)
        self.assertGreater(len(retrieved_docs), 0)


if __name__ == "__main__":
    unittest.main()
