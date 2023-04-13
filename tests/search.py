import unittest
from src.search import binary_search

class SearchTests(unittest.TestCase):
    def test_binary_search(self):
        sorted_lyst = [2, 5, 8, 9, 13, 15, 18, 30]
        result = binary_search(13, sorted_lyst)
        self.assertEqual(result, 4)

    def test_binary_search_not_found(self):
        sorted_lyst = [2, 5, 8, 9, 13, 15, 18, 30]
        result = binary_search(1, sorted_lyst)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
