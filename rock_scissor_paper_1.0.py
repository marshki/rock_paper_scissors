#!/bin/py 
#Python 2.7.6
"""A text-based Python 2.7.6 implementation of the game Rock-Paper-Scissors.

Game play:  
        * each round, both players select from: rock, paper, or scissors 
        * rock beats scissors, scissors beats paper, paper beats rock 
        * a player receives 1 point per round (s)he wins
        * 0 points for ties 
        * first player to win user designated number of rounds is the victor 
"""

# Import libraries  
import sys						# work with runtime environment  
from random import choice 				# to randomize bot moves 

# Declarations 
moves = ["r", "p", "s"] 				# Possible moves  

winning_combos = {("r", "s"), ("s", "p"), ("p", "r")} 	# Winning outcomes 

human_score, bot_score = 0 , 0 				# Initialize player scores 

# Define functions 

def rounds():
	""" Prompt user for number of rounds to play"""
	while True:
		try: 
			num_rounds = int(raw_input("Type the number of rounds you want to play, and press Enter: "))
			print "Cool! Let\'s play %d round(s) of Rock-Paper-Scissors." %num_rounds
			return num_rounds 
		except: 							
			print "Sorry, that\'s not a valid number. Please try again."


def human():		
	""" Prompt user for input, and limit options to acceptable moves."""
	while True:
		print "R: Rock    P: Paper    S: Scissor    Q: Quit" 	# Possible moves
		human_move = raw_input("Enter your choice: ").lower()	# convert input to lower case variation
		
		if human_move in moves or human_move == "q": 		# acceptable moves 
			return human_move 
		else: 										
			print "Sorry, that\'s invalid input." 


def bot():	
	""" Randomize bot's move.""" 
	bot_move = choice(moves)					
	return bot_move


def game_over():	
	""" Game over when either player wins user defined number of rounds first."""
	if bot_score == game_length: 								
		print "The bot wins, you puny human. " 
		sys.exit() 
	elif human_score == game_length: 
		print "The puny human wins." 
		sys.exit()

print"""
********** Welcome to Rock-Paper-Scissors! **********

See if you can beat the bot!

Keep in mind:
        * rock breaks scissors,
        * scissors cut paper,
        * paper covers rock.

Good luck!
"""

def gameplay(): 

	game_length = rounds()
		
	while True:					# Compare output of players, decide on winner, and keep score 
		
		hu, bo  = human(), bot()
	
		if hu == "q":				# Allow user to quit at anytime
			sys.exit(0) 

		if  hu == bo:				# conditions for a tie  
			print "You both choose %s. Grr... a tie!" % (bo)
			print "Your score:%s Bot score:%s" %(human_score, bot_score)

        	elif (hu, bo) in winning_combos:	# conditions for user win 
               		print "You picked %s and the bot picked %s. Woo-hoo! You win this one, human." %(hu, bo)
			human_score += 1
			print "Your score:%s Bot score:%s" %(human_score, bot_score)

        	else:					# conditions for bot win 
			print "You picked %s and the bot picked %s. Bwahahaha! The almighty bot wins!" %(hu, bo)
			bot_score += 1
			print "Your score:%s Bot score:%s" %(human_score, bot_score)

		game_over()			# conditions for game over 

gameplay()
