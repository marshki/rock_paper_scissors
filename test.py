#!/bin/py
def rounds():
	while True: 
		rounds = raw_input("How many rounds of Rock-Paper-Scissors would you like to play?: ")
		try: 
			rounds = int(rounds)
			print "Cool! Let\'s play %d rounds of Rock-Paper-Scissors." %rounds 
			return rounds 
		except:
			print "Sorry, that\'s not a valid number. Please try again."  
rounds()
