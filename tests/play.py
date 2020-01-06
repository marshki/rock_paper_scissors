#!/usr/bin env python

"""Unit testing class.
"""
import unittest

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
            print("\nThe bot wins, you puny human. ")
            break

        elif SCORES['human'] == GAME_LENGTH:
            print("\nThe puny human wins.")
            break

#class Play(unitest.TestCase):
    """Unit test.
    """

    #def test_play(self, input):
        """Placeholder.
        """

if __name__ == '__main__':
    unittest.main()
