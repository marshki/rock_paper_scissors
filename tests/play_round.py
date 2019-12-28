#!/usr/bin/env python

"""Unit testing class.
"""

from __future__ import print_function
from builtins import input
from random import choice

MOVES = ["r", "p", "s"]
WINNING_COMBOS = [("r", "s"), ("p", "r"), ("s", "p")]
SHOW_VALID_MOVES = "R: Rock    P: Paper    S: Scissors    Q: Quit"

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

def player1():
    """Prompt user for input and evaluate.
    Return move if in acceptable moves ('r', 'p', 's', 'q')
    """
    valid_input = MOVES + ['q']

    while True:

        print()
        print(SHOW_VALID_MOVES)

        player1_move = input("Enter your choice: ").lower()

        if player1_move not in valid_input:
            print("Sorry, that\'s invalid input. Try again: ")
        else:
            return player1_move

def player2():
    """Randomize bot's move.
    Return move.
    """
    player2_move = choice(MOVES)

    return player2_move
"""
def play_round():
    Evalute human and bot move to determine win or tie.
    Return 'human' or 'bot' move if winner, else replay.

    while True:
        human, bot  = player1(), player2()

        if human == "q":
            return human

        if  human == bot:            
            print("\nYou both chose {}. Grr... a tie!".format(bot))

        elif (human, bot) in WINNING_COMBOS:
            print("\nYou picked {} and the bot picked {}.".format(human, bot), 
                  "\nWoo-hoo! You win this one, human.")
            return 'human'

        else
            print("\nYou picked {} and the bot picked {}.".format(human, bot), 
                  "\nBwahahaha! The almighty bot wins!")            
            return 'bot'

if __name__ == '__main__':
play_round()
"""
