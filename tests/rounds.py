#!/usr/bin/env python

"""Unit testing class.
"""

import unittest
from unittest.mock import patch

def rounds():
    """Prompt user.
    Return number of rounds as integer.
    """

    while True:
        try:
            return int(input("Type the number of rounds to play and press enter: "))
        except ValueError:
            print("Sorry, that\'s invalid input. Try again: ")
            raise

class Rounds(unittest.TestCase):

    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='10')
    def test_rounds_01(self, input):
        """Valid return value.
        """
        self.assertIsInstance(rounds(), int)

    @patch('builtins.input', return_value='Derp!')
    def test_rounds_02(self, input):
        """Invalid return value.
        """
        with self.assertRaises(ValueError):
            rounds()

if __name__ == '__main__':
    unittest.main()
