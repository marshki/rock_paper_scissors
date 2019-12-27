#!/usr/bin/env python

"""Unit test.
"""

from __future__ import print_function
from builtins import input

def rounds():
    """Prompt user.
    Return number of rounds as integer.
    """
    while True:
        try:
            num_rounds = int(input("Type the number of rounds to play and press enter: "))
            print("O.K. Let\'s play {} round(s)".format(num_rounds))
            return num_rounds

        except ValueError:
            print("Sorry, that\'s invalid input. Try again: ")

if __name__ == '__main__':
    rounds()
