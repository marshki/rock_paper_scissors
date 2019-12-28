#!/usr/bin/env python

"""Unit test suite.
"""

MOVES = ["r", "p", "s"]
SHOW_VALID_MOVES = "R: Rock    P: Paper    S: Scissors    Q: Quit"

def player1():
    """Prompt user for input, and limit options to acceptable moves."""
    valid_input = MOVES + ['q']

    while True:

        print()
        print(SHOW_VALID_MOVES)

        player1_move = input("Enter your choice: ").lower()

        if player1_move not in valid_input:
            print("Sorry, that\'s invalid input. Try again: ")

        else:
            return player1_move

if __name__ == '__main__':
    player1()
