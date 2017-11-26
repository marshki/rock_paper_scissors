from __future__ import print_function 
from builtins import input 

#!/usr/bin/env python 

def rounds():
    """Prompt user for rounds of play"""
    while True:
        try:
            num_rounds = int(input("Type the number of rounds to play and press enter: "))
            print ("O.K. Let\'s play {} round(s)".format(num_rounds))
            return num_rounds

        except ValueError:
            print("Sorry, that\'s invalid input. Try again: ")

if __name__ == '__main__':
	rounds()
