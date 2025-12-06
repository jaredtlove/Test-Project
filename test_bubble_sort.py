import unittest
from bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sort_random(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bubble_sort(arr), expected)

    def test_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected)

    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected)

    def test_empty_list(self):
        arr = []
        expected = []
        self.assertEqual(bubble_sort(arr), expected)

    def test_single_element(self):
        arr = [1]
        expected = [1]
        self.assertEqual(bubble_sort(arr), expected)

    def test_duplicates(self):
        arr = [3, 1, 2, 3, 1]
        expected = [1, 1, 2, 3, 3]
        self.assertEqual(bubble_sort(arr), expected)

    def test_negative_numbers(self):
        arr = [-1, -5, 2, 0, 3]
        expected = [-5, -1, 0, 2, 3]
        self.assertEqual(bubble_sort(arr), expected)

if __name__ == '__main__':
    unittest.main()
