#!/usr/bin env python

"""Unit testing class.
"""

GAME_LENGTH = 1
SCORES = {'human':0, 'bot':0}

RESULT = 'bot'

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
play()

"""There are two items that need to be tested:
- does the score counter work? (yes)
- does the game end when it should? (yes, but we need to run a simulation of the while loop)

class_Play(unitest.TestCase):
    Unit test.

    def test_play():
        Placeholder.
"""
