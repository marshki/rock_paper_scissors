#!/usr/bin/env python
# pylint: disable=W0613,W0622

"""Unit testing class.
"""

import unittest
from unittest.mock import patch
from random import choice

MOVES = ["r", "p", "s"]

def player2():
    """Randomize bot's move.
    """
    player2_move = choice(MOVES)

    return player2_move

class Player2(unittest.TestCase):
    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='r')
    def test_player2_01(self, input):
        """Valid return value.
        """
        self.assertIn(player2(), ['r', 'p', 's'])

    @patch('builtins.input', return_value='s')
    def test_player2_02(self, input):
        """Valid return value.
        """
        self.assertIn(player2(), ['r', 'p', 's'])

if __name__ == '__main__':
    unittest.main()
