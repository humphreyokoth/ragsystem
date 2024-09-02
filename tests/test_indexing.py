import unittest
from src.indexing import index_text


class TestIndexing(unittest.TestCase):
    def test_index_text(self):
        text = "This is a test document."
        index_text(text, index_name="test_index")


if __name__ == "__main__":
    unittest.main()
