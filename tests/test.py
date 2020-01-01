"""Seed values to run simulation.
For reference:
  - rock beats scissors
  - scissors beats paper
  - paper beats rock.
"""

import unittest

HUMAN_ROUND1 = ['r', 'p', 's']
BOT_ROUND1 = ['s', 'r', 'p']

HUMAN_ROUND2 = ['s', 's', 'r', 'p']
BOT_ROUND2 = ['s', 'r', 'p', 's']

WINNING_COMBOS = [('r', 's'), ('p', 'r'), ('s', 'p')]

ZIPPED1 = zip(HUMAN_ROUND1, BOT_ROUND1)
ZIPPED2 = zip(HUMAN_ROUND2, BOT_ROUND2)

def evaluate_round(_i):
    """Placeholder.
    """
    if _i in WINNING_COMBOS:
        return True
    else:
        return False

class EvaluateRound(unittest.TestCase):
    """Unit tests.
    """
    def test_evaluate_round1(self):
        """Placeholder.
        """
        for _i in ZIPPED1:
            with self.subTest(_i=_i):
                self.assertTrue(evaluate_round(_i))

    def test_evaluate_round2(self):
        """Placeholder.
        """
        for _i in ZIPPED2:
            with self.subTest(_i=_i):
                self.assertFalse(evaluate_round(_i))

if __name__ == '__main__':
    unittest.main()
