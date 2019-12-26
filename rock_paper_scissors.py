#!/usr/bin/env python

"""A text-based implementation of Rock-Paper-Scissors in Python 2 & 3.
"""

from __future__ import print_function
from builtins import input
from random import choice

MOVES = ["r", "p", "s"]
WINNING_COMBOS = [("r", "s"), ("p", "r"), ("s", "p")]
SHOW_VALID_MOVES = "R: Rock    P: Paper    S: Scissors    Q: Quit"

def rounds():
    """Prompt user.
    Return number of rounds as int.
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
    Return move if in acceptable moves ('r', 'p', 's', 'q').
    """
    valid_input = MOVES + ['q']

    while True:

        print()
        print(SHOW_VALID_MOVES)

        player1_move = input("Enter your choice: ").lower()

        if player1_move in valid_input:
            return player1_move

        else: 
            print("Sorry, that\'s invalid input. Try again: ")

def player2():
    """Randomize bot's move.
    Return move.
    """
    player2_move = choice(MOVES)

    return player2_move

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
            print("You picked {} and the bot picked {}."
                  "Woo-hoo! You win this one, human.".format(human, bot))
            return 'human'

        else:
            print("You picked {} and the bot picked {}."
                  "Bwahahaha! The almighty bot wins!".format(human, bot))
            return 'bot'

def play():
    """Game play.
    Evaluate length of game, and track score.
    """

    game_length = rounds()
    scores = {'human':0, 'bot':0}

    while True:
        result = play_round()
        if result == 'q':
            break

        scores[result] += 1
        print("Your score: {human}, Bot score: {bot}".format(**scores))

        if scores['bot'] == game_length:
            print("\nThe bot wins, you puny human. ")
            break

        elif scores['human'] == game_length:
            print("\nThe puny human wins.")
            break

if __name__ == '__main__':

    print("""
********** Welcome to Rock-Paper-Scissors **********
See if you can beat the bot!
Keep in mind:
* rock breaks scissors,
* scissors cut paper,
* paper covers rock.
Good luck!
    """)

play()
