import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_found_middle(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3), 2)

    def test_found_start(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 1), 0)

    def test_found_end(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 5), 4)

    def test_not_found_less(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 0), -1)

    def test_not_found_greater(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 6), -1)

    def test_not_found_middle(self):
        arr = [1, 3, 5]
        self.assertEqual(binary_search(arr, 2), -1)

    def test_empty_list(self):
        arr = []
        self.assertEqual(binary_search(arr, 1), -1)

    def test_single_element_found(self):
        arr = [1]
        self.assertEqual(binary_search(arr, 1), 0)

    def test_single_element_not_found(self):
        arr = [1]
        self.assertEqual(binary_search(arr, 2), -1)

if __name__ == '__main__':
    unittest.main()
