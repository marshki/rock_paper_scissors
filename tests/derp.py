"""Placeholder.
"""

HUMAN_MOVE = ['r', 'p', 's', 's', 's', 'r', 'p', 'r', 's']
BOT_MOVE = ['s', 'r', 'p', 's', 'r', 'p', 's', 's', 'p']
ROUND = zip(HUMAN_MOVE, BOT_MOVE)

WINNING_COMBOS = [('r', 's'), ('p', 'r'), ('s', 'p')]
RESULT = []

for _i in ROUND:
    if _i in WINNING_COMBOS:
        RESULT.append(bool(_i))
    else:
        RESULT.append(bool())

print(RESULT)
