#!/usr/bin/python3
"""Unittests for 6-max_integer_test"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def is_ordered(self):
        """Test an ordered list"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def is_unordered(self):
        """Test an unordered list"""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def is_max_beginning(self):
        """max beginning."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def is_empty(self):
        """empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def is_one(self):
        """one element list"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def is_float(self):
        """float tests."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def is_mixed(self):
        """ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def is_string(self):
        """string."""
        string = "Mourad"
        self.assertEqual(max_integer(string), 'r')

    def is_str_list(self):
        """strings."""
        strings = ["Call", "me", "maybe?", "?"]
        self.assertEqual(max_integer(strings), "N")

    def is_empty2(self):
        """empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()