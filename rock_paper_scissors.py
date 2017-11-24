from __future__ import print_function
from builtins import input

#!/usr/bin/env python
# mjk 2016.05.09

"""
A text-based implementation of Rock-Paper-Scissors in Python 2 & 3.

Game play:

* Player defines number of rounds to play.
* Each round, player selects from: rock, paper, or scissors.
* Rock beats scissors, scissors beats paper, paper beats rock.
* Player receives 1 point per round won.
* 0 points awarded for ties, and round must be replayed.
* First player to win user defined number of rounds is the victor.
"""

from random import choice                                           # To ramdomize "bot" moves

MOVES = ["r", "p", "s"]                                             # Possible moves
WINNING_COMBOS = {("r", "s"), ("p", "r"), ("s", "p")}               # Winning scenarios
SHOW_VALID_MOVES = "R: Rock    P: Paper    S: Scissor    Q: Quit"   # Display to user

def rounds():
    """Prompt user for rounds of play"""
    while True:
        try:
            num_rounds = int(input("Type the number of rounds to play and press Enter: "))
            return num_rounds

            print ("Let\'s play {} round(s) of Rock-Paper-Scissors!".format(num_rounds))    ###Can we place this elsewhere?###

        except ValueError:
            print("Sorry, that\'s invalid input. Try again: ")

def player1():
    """Prompt user for input, and limit options to acceptable moves."""
    valid_input = MOVES + ['q']
    while True:

        print(SHOW_VALID_MOVES)                                                             ###Can we places this elsewhere?###

        player1_move = input("Enter your choice: ").lower()

        if player1_move in valid_input:
            return player1_move
        else:
            print("Sorry, that\'s invalid input. Try again: " )

def player2():
    """Randomize bot's move."""
    player2_move = choice(MOVES)
    return player2_move

def play_round():
    """Play a single round and either return the winner's name or 'q' to retire"""

    while True:                             # while loop to compare output of players, decide on winner, and keep score
        human, bot  = player1(), player2()

        if human == "q":                       # Allow user to quit at anytime
            return human

        if  human == bot:                       # conditions for a tie
            print("You both chose {}. Grr... a tie!".format(bot))

        elif (human, bot) in WINNING_COMBOS:    # conditions for user win
            print("You picked {} and the bot picked {}. Woo-hoo! You win this one, human.".format(human, bot))
            return 'human'

        else:                               # conditions for bot win
            print("You picked {} and the bot picked {}. Bwahahaha! The almighty bot wins!".format(human, bot))
            return 'bot'

def play():
    print("""
********** Welcome to Rock-Paper-Scissors! **********
 See if you can beat the bot!
 Keep in mind:
* rock breaks scissors,
* scissors cut paper,
* paper covers rock.
Good luck!
    """)

    game_length = rounds()                              # number of rounds
    scores = {'human':0, 'bot':0}                       # initialize scores
    while True:
        result = play_round()
        if result == 'q':                               # allow user to end game
            break

        scores[result] += 1                             # update score
        print("Your score: {human}, Bot score: {bot}".format(**scores))
        if scores['bot'] == game_length:                # bot wins == user defined number of rounds
            print("The bot wins, you puny human. " )
            break
        elif scores['human'] == game_length:            # human wins == user defined number of rounds
            print("The puny human wins." )
            break

if __name__ == '__main__':                              # let the games begin
    play()
'''
