#
# cointoss.py - simulate tossing a coin multiple times
#

import random

coin = ['heads', 'tails']
heads = 0
tails = 0

print('\nCOIN TOSS\n')

entered_trials = input('Enter how many times you want to flip the coin: ')
trials = int(entered_trials)


for index in range(trials):
    if random.choice(coin) == 'heads':
        heads = heads + 1
    else:
        tails = tails + 1

print('\nThere were ', heads, ' heads and ', tails, ' tails.\n')
