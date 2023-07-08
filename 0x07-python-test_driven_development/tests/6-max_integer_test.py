#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    """Testing empty list."""
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    """Testing list with one element."""
    def test_list_with_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    """Testing list with multiple elements."""
    def test_list_with_multiple_elements(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    """Testing list with duplicate elements."""
    def test_list_with_duplicate_elements(self):
        self.assertEqual(max_integer([1, 1, 2, 3, 4]), 4)

if __name__ == '__main__':
    unittest.main()
