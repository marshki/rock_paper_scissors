"""Seed values to run simulation.
"""

HUMAN = ['r', 'p', 's', 's', 's', 'r', 'p']
BOT = ['s', 'r', 'p', 's', 'r', 'p', 's']

WINNING_COMBOS = [('r', 's'), ('p', 'r'), ('s', 'p')]

MAPPED = zip(HUMAN, BOT)
#print(MAPPED)

REMAPPED = set(MAPPED)
#print(REMAPPED)

for _i in REMAPPED:
    print(_i)
