#
# numbersbar.py: Read 10 numbers, store values using arrays and plot as a bar chart
#
import numpy as np

import matplotlib.pyplot as  plt

numarray = np.zeros(10)  # creats an empty 10 element array

print('Enter 10 numbers ')

for i in range(len(numarray)):
    print('Enter a number (', i, ') ')
    numarray[i] = int(input())

plt.title('Numbers Bar Chart')
plt.xlabel('Index')
plt.ylabel('Number')
plt.bar([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], numarray, 0.9, color = 'purple')
plt.show()
