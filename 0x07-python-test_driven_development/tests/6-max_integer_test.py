"""This module is the test suites fot the 'max_integer' function
to return the maximum integer in a list
"""
# import the unittest module and the function
import unittest
max_integer = __import__('6-max_integer').max_integer


class testMaxInteger(unittest.TestCase):
    """The class for testing max_integer function"""
    def test_list_empty(self):
        # Check if the list is empty
        self.assertIsNone(max_integer([]))
