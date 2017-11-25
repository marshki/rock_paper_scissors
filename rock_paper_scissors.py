from __future__ import print_function
from builtins import input

#!/usr/bin/env python
# mjk 2016.05.09

"""
A text-based implementation of Rock-Paper-Scissors in Python 2 & 3.

* Rock beats scissors, scissors beats paper, paper beats rock.
* Player receives 1 point per round won. 0 points awarded for ties, and round must be replayed.
* First player to win user defined number of rounds is the victor.
"""

from random import choice                                            # randomize "bot" moves

MOVES = ["r", "p", "s"]                                              # possible moves
WINNING_COMBOS = {("r", "s"), ("p", "r"), ("s", "p")}                # winning scenarios
SHOW_VALID_MOVES = "R: Rock    P: Paper    S: Scissors    Q: Quit"   # display to player1

def rounds():
    """Prompt user for rounds of play"""
    while True:
        try:
            num_rounds = int(input("Type the number of rounds to play and press enter: "))
            print ("O.K. Let\'s play {} round(s)".format(num_rounds))
            return num_rounds

        except ValueError:
            print("Sorry, that\'s invalid input. Try again: ")

def player1():
    """Prompt user for input, and limit options to acceptable moves."""
    valid_input = MOVES + ['q']
    while True:

        print()
        print(SHOW_VALID_MOVES)

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
    """Play a single round and return outcome, or quit"""

    while True:                                     # while loop to compare output of players, decide on winner, and keep score
        human, bot  = player1(), player2()

        if human == "q":                            # allow user to quit at anytime
            return human

        if  human == bot:                           # conditions for a tie
            print("\nYou both chose {}. Grr... a tie!".format(bot))

        elif (human, bot) in WINNING_COMBOS:        # conditions for user win
            print("\nYou picked {} and the bot picked {}. Woo-hoo! You win this one, human.".format(human, bot))
            return 'human'

        else:                                       # conditions for bot win
            print("\nYou picked {} and the bot picked {}. Bwahahaha! The almighty bot wins!".format(human, bot))
            return 'bot'

def play():

    game_length = rounds()                          # number of rounds
    scores = {'human':0, 'bot':0}                   # initialize score

    while True:
        result = play_round()
        if result == 'q':                           # allow user to end game
            break

        scores[result] += 1                         # update score
        print("Your score: {human}, Bot score: {bot}".format(**scores))

        if scores['bot'] == game_length:            # bot wins == user defined number of rounds
            print("\nThe bot wins, you puny human. " )
            break

        elif scores['human'] == game_length:        # human wins == user defined number of rounds
            print("\nThe puny human wins." )
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
