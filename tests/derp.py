"""Placeholder.
"""

HUMAN_MOVE = ['r', 'p', 's', 's', 's', 'r', 'p']
BOT_MOVE = ['s', 'r', 'p', 's', 'r', 'p', 's']
ROUND = zip(HUMAN_MOVE, BOT_MOVE)

WINNING_COMBOS = [('r', 's'), ('p', 'r'), ('s', 'p')]
RESULT = []

for _i in ROUND:
    print(_i)
    if _i in WINNING_COMBOS:
        RESULT.append('True')
    else:
        RESULT.append('False')

print(RESULT)
