from __future__ import print_function			
from builtins import input				 

#!/bin/py 
#Python 2 & 3 

"""A text-based Python 2 & 3 implementation of the game Rock-Paper-Scissors.
Game play:  
        * each round, both players select from: rock, paper, or scissors 
        * rock beats scissors, scissors beats paper, paper beats rock 
        * a player receives 1 point per round (s)he wins
        * 0 points for ties 
        * first player to win user designated number of rounds is the victor 
"""

# Import libraries  

from random import choice 				# to randomize bot moves 

# Declarations 

MOVES = ["r", "p", "s"] 				# Possible moves  

WINNING_COMBOS = {("r", "s"), ("s", "p"), ("p", "r")} 	# Winning outcomes 

# Define functions 

def rounds():
	""" Prompt user for number of rounds to play"""
	while True:
		try: 
			num_rounds = int(input("Type the number of rounds you want to play, and press Enter: "))
			print("Cool! Let\'s play %d round(s) of Rock-Paper-Scissors." %num_rounds)
			return num_rounds 
        	except ValueError: 							
			print ("Sorry, that\'s not a valid number. Please try again.")


def human():		
    """ Prompt user for input, and limit options to acceptable moves."""
    valid = MOVES + ['q']
    while True:
        print ("R: Rock    P: Paper    S: Scissor    Q: Quit")
        human_move = input("Enter your choice: ").lower()
		
        if human_move in valid:
            return human_move 
        else: 							
            print("Sorry, that\'s invalid input." )


def bot():	
	""" Randomize bot's move.""" 
	bot_move = choice(MOVES)					
	return bot_move


def play_round():
    '''play a single round and either return the winner's name or 'q' to retire'''
    while True:					# while loop to compare output of players, decide on winner, and keep score 
        hu, bo  = human(), bot()
        if hu == "q":				# Allow user to quit at anytime
            return hu
        if  hu == bo:				# conditions for a tie  
            print("You both choose %s. Grr... a tie!" % (bo))
        elif (hu, bo) in WINNING_COMBOS:	# conditions for user win 
            print("You picked %s and the bot picked %s. Woo-hoo! You win this one, human." %(hu, bo))
            return 'human'
        else:					# conditions for bot win 
            print("You picked %s and the bot picked %s. Bwahahaha! The almighty bot wins!" %(hu, bo))
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

    game_length = rounds()
    scores = {'human':0, 'bot':0}
    while True:
        result = play_round()
        if result == 'q':
            break

        scores[result] += 1
        print("Your score: {human}, Bot score: {bot}".format(**scores))
        if scores['bot'] == game_length:
            print("The bot wins, you puny human. " )
            break
        elif scores['human'] == game_length: 
            print("The puny human wins." )
            break

if __name__ == '__main__':
    play()
