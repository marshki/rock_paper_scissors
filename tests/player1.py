#!/usr/bin/env python
# pylint: disable=W0613,W0622

"""Unit testing class.
"""

import unittest
from unittest.mock import patch

MOVES = ["r", "p", "s"]

def player1():
    """Prompt user for input, and limit options to acceptable moves.
    """

    valid_input = MOVES + ['q']

    while True:

        player1_move = input("Enter your choice: ").lower()

        if player1_move not in valid_input:
            print("Sorry, that\'s invalid input. Try again: ")

        else:
            return player1_move

class Player1(unittest.TestCase):
    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='r')
    def test_player1_01(self, input):
        """Valid return value.
        """
        self.assertIn(player1(), ['valid_input'])

    @patch('builtins.input', return_value='x')
    def test_player1_02(self, input):
        """Valid return value.
        """
        self.assertNotIn(player1(), 'valid_input')

if __name__ == '__main__':
    unittest.main()
