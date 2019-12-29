#!/usr/bin/env python

"""Unit testing class.
"""

from __future__ import print_function
from builtins import input
import unittest
from unittest.mock import patch

WINNING_COMBOS = [("r", "s"), ("p", "r"), ("s", "p")]

def play_round():
    """Evaluate human and bot move to determine win or tie.
    Return 'human' or 'bot' move if winner, else replay.
    For reference:
      - rock beats scissors
      - scissors beats paper
      - paper beats rock.
    """

    while True:
        human, bot = player1(), player2()

        if human == "q":
            return human

        if  human == bot:
            print("\nYou both chose {}. Grr... a tie!".format(bot))

        elif (human, bot) in WINNING_COMBOS:
            print("\nYou picked {} and the bot picked {}.".format(human, bot),
                  "\nWoo-hoo! You win this one, human.")
            return 'human'

        else:
            print("\nYou picked {} and the bot picked {}.".format(human, bot),
                  "\nBwahahaha! The almighty bot wins!")
            return 'bot'

class PlayRounds(unittest.TestCase):
    """Unit tests.
    Use `patch()` to mock objects for testing.
    For reference: https://docs.python.org/3/library/unittest.mock.html
    """

    @patch('builtins.input', return_value='r')
    def test_play_rounds_01(self, input):
        """Valid return value.
        """
       
if __name__ == '__main__':
    play_round()
