#!/usr/bin/env python

"""Unit testing class.
"""

import unittest

HUMAN_MOVE = ['r', 'p', 's', 's', 's']
BOT_MOVE = ['s', 's', 'p', 's', 'r']

ROUND = zip(HUMAN_MOVE, BOT_MOVE)

WINNING_COMBOS = [('r', 's'), ('p', 'r'), ('s', 'p')]

EXPECTED_RESULT = [True, False, True, False, False]
RESULT = []

def play_round():
    """Simulate rounds of play.
    Return boolean value to RESULT.
    """
    for _i in ROUND:
        if _i in WINNING_COMBOS:
            RESULT.append(bool(_i))
        else:
            RESULT.append(bool())

play_round()

class PlayRound(unittest.TestCase):
    """Testing class.
    """
    def test_play_round(self):
        """Compare RESULT, EXPECTED_RESULT.
        """
        self.assertListEqual(RESULT, EXPECTED_RESULT)

if __name__ == '__main__':
    unittest.main()
