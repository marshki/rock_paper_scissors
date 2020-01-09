#!/usr/bin env python
# pylint: disable=W0613,W0622

"""Unit testing class.
"""
import unittest
from unittest.mock import patch

GAME_LENGTH = 3
SCORES = {'human':0, 'bot':0}

RESULT = ('bot')

def play():
    """Placeholder.
    """
    while True:
        SCORES[RESULT] += 1
        print("Your score: {human}, Bot score: {bot}".format(**SCORES))

        if SCORES['bot'] == GAME_LENGTH:
            return "The bot wins, you puny human."

        if SCORES['human'] == GAME_LENGTH:
            return "The puny human wins."

class Play(unittest.TestCase):
    """Unit test.
    """
    @patch('builtins.input', return_value='')
    def test_play(self, input):
        """Placeholder.
        """
        self.assertEqual(play(), "The bot wins, you puny human.")

if __name__ == '__main__':
    unittest.main()
