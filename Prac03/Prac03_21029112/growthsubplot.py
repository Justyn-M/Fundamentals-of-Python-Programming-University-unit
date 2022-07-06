#
# growthplot.py - plotting a graph of a simulation of unconstrained growth
#

import matplotlib.pyplot as plt
import numpy as np

march2017 = np.array([37.7, 29.9, 35.2, 36.2, 36.2, 34.7, 33.8, 34.5, 31.9, 29.9, 30.9, 24.8, 24.2, 24.1, 24.0])

print("\nSIMULATION - March Temperatures\n")

dates = range(1, len(march2017)+1)

plt.figure(1)
plt.subplot(221)
plt.plot(dates, march2017, '--')
plt.ylabel('Temperature')

plt.subplot(222)
plt.plot(dates, march2017, 'ro')
plt.title('March Temperatures')
plt.ylabel('Temperature')
plt.xlabel('Date')

plt.subplot(223)
plt.plot(dates, march2017, 'g')
plt.title('March Temperatures')
plt.ylabel('Temperature')
plt.xlabel('Date')

plt.subplot(224)
plt.plot(dates, march2017, 'bs')
plt.title('March Temperatures')
plt.ylabel('Temperature')
plt.xlabel('Date')

plt.show()
