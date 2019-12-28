#!/usr/bin/env python

"""Unit test suite.
"""

from random import choice

MOVES = ["r", "p", "s"]

def player2():
    """Randomize bot's move.
    """
    player2_move = choice(MOVES)

    return player2_move

if __name__ == '__main__':
    player2()
