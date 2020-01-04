"""Placeholder.
"""

import unittest

HUMAN_MOVE = ['r', 'p', 's', 's', 's']
BOT_MOVE = ['s', 's', 'p', 's', 'r']

ROUND = zip(HUMAN_MOVE, BOT_MOVE)

WINNING_COMBOS = [('r', 's'), ('p', 'r'), ('s', 'p')]

EXPECTED_RESULT = [True, False, True, False, False]
RESULT = []

def evaluate_round():
    """Placeholder.
    """
    for _i in ROUND:
        if _i in WINNING_COMBOS:
            RESULT.append(bool(_i))
        else:
            RESULT.append(bool())

evaluate_round()

class EvaluateRound(unittest.TestCase):
    """Placeholder.
    """
    def test_evaluate_round(self):
        """Placeholder.
        """
        self.assertListEqual(RESULT, EXPECTED_RESULT)

if __name__ == '__main__':
    unittest.main()
