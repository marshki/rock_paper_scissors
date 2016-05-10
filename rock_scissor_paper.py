#!/bin/py 
#Python 2.7.6

"""A text-based Python 2.7.6 implementation of the game Rock-Paper-Scissors.

Game play:  
        * each round, both players select from: rock, paper, or scissors 
        * rock beats scissors, scissors beats paper, paper beats rock 
        * a player receives 1 point per round (s)he wins
        * 0 points for ties 
        * first player to reach 5 points wins. 
"""
# Import libraries  
import sys 
from random import choice 

# Declarations 
moves = ["r", "p", "s"] # Possible moves  

winning_combos = {("r", "s"), ("s", "p"), ("p", "r")} # Winning outcomes 

human_score, bot_score = 0, 0 # Initialize player scores 

# Welcome screen 
print"""
********** Welcome to Rock-Paper-Scissors! **********

See if you can win five rounds before the bot.

Keep in mind:
        * rock breaks scissors,  
        * scissors cut paper, 
        * paper covers rock. 

Good luck!
"""

# Define functions 
def human():	# Prompt for user input. Accept upper and lower variants
	print 
	print "R: Rock    P: Paper    S: Scissor" 
	human_move = raw_input("Enter your choice: ").lower()
	return human_move 
()

def bot():	# Randomize bot's move 
	bot_move = choice(moves)
	return bot_move
()

def game_over():	# Game over when either player scores five points 
	if bot_score == 5: 
		print 
		print "The bot wins, you puny human. " 
		sys.exit() 
	elif human_score == 5: 
		print
		print "The puny human wins." 
		sys.exit()
()

# The program 
while True:	# While loop to compare output of players, decide on winner, and keep score 
	hu, bo  = human(), bot()
	
	if  hu == bo:
		print 
		print "You both choose %s. Grr... a tie!" % (bo)
		print "Your score:%s Bot score:%s" %(human_score, bot_score)
        elif (hu, bo) in winning_combos:
		print 
                print "You picked %s and the bot picked %s. Woo-hoo! You win this one, human." %(hu, bo)
		human_score += 1
		print "Your score:%s Bot score:%s" %(human_score, bot_score)
        else:
                print 
		print "You picked %s and the bot picked %s. Bwahahaha! The almighty bot wins!" %(hu, bo)
		bot_score += 1
		print "Your score:%s Bot score:%s" %(human_score, bot_score)

	game_over()	
