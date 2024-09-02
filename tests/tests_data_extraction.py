import unittest
from src.data_extraction import extract_text_from_google_docs


class TestDataExtraction(unittest.TestCase):
    def test_extract_text_from_google_docs(self):
        text = extract_text_from_google_docs()
        self.assertIsNotNone(text)
        self.assertGreater(len(text), 0)


if __name__ == "__main__":
    unittest.main()
