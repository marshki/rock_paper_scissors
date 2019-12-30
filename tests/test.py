"""Seed values to run simulation.
For reference:
      - rock beats scissors
      - scissors beats paper
      - paper beats rock.
"""

HUMAN = ['r', 'p', 's', 's', 's', 'r', 'p']
BOT = ['s', 'r', 'p', 's', 'r', 'p', 's']

WINNING_COMBOS = [('r', 's'), ('p', 'r'), ('s', 'p')]

ZIPPED = zip(HUMAN, BOT)

for _i in ZIPPED:
    print(_i)
    if _i in WINNING_COMBOS:
        print('True')
    else: 
        print('False')
