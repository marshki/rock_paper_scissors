"""Seed values to run simulation.
For reference:
  - rock beats scissors
  - scissors beats paper
  - paper beats rock.
"""

import unittest

HUMAN = ['r', 'p', 's', 's', 's', 'r', 'p']
BOT = ['s', 'r', 'p', 's', 'r', 'p', 's']

WINNING_COMBOS = [('r', 's'), ('p', 'r'), ('s', 'p')]

ZIPPED = zip(HUMAN, BOT)

def evaluate_round(_i):
    """Placeholder.
    """
    if _i in WINNING_COMBOS:
        return True
    else:
        return False

#for _i in ZIPPED:
#    evaluate_round(_i)

class EvaluateRound(unittest.TestCase):
    """Unit tests.
    """
    def test_evaluate_round(self):
        """Placeholder.
        """
        for _i in ZIPPED:
            with self.subTest(_i=_i):
                self.assertTrue(evaluate_round(_i))

if __name__ == '__main__':
    unittest.main()
