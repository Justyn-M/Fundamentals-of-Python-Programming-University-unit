#
# numbersarray.py: Read 10 numbers give sum, min, max, mean and plot numbers on graph
#

import numpy as np 

import matplotlib.pyplot as plt

numarray = np.zeros(10)  # creats an empty 10 element array

print('Enter 10 numbers ')

for i in range(len(numarray)):
    print('Enter a number (', i, ') ')
    numarray[i] = int(input())

print('Total is', numarray.sum())

print('Minimum is', numarray.min())

print('Maximum is', numarray.max())

print('Mean is', numarray.mean())

plt.title('Number of times a number is entered')
plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numarray, color = 'blue')
plt.show()
