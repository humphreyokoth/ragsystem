import unittest
from src.generation import generate_response


class TestGeneration(unittest.TestCase):
    def test_generate_response(self):
        retrieved_docs = [{"_source": {"text": "This is a test document."}}]
        response = generate_response(retrieved_docs)
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)


if __name__ == "__main__":
    unittest.main()
