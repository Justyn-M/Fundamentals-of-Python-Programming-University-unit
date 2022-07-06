#
# growtharray.py - simulation of unconstrained growth, using arrays to store values
#

import numpy as np
import matplotlib.pyplot as plt

zeroarray = np.zeros(100)

print("\nSIMULATION - Unconstrianed Growth\n")

length = 10
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = length / time_step
growth_step = growth_rate * time_step

print('INITIAL VALUES:\n')
print('Simulation Length (hours): ', length)
print('Initial Population: ', population)
print('Growth Rate (per hour): ', growth_rate)
print('Time Step (part hour per step): ', time_step)
print('Num iterations (sim length * time step per hour): ', num_iter)
print('Growth step (growth rate per item step): ', growth_step)

print('\nRESULTS:\n')

print('Time: ', 0, ' \tGrowth: ', 0, ' \tPopulation: ', 100)
times =[0]
pops=[100]

for i in range(1, int(zeroarray)):
    growth = growth_step * population
    population = population + growth
    time = i * time_step
    times.append(time)
    zeroarray.append(population)
    print('Time: ', time, ' \tGrowth: ', growth, ' \tPopulation: ', population)

print('\nPROCESSING COMPLETE.\n')

plt.title('Unconstrained Growth')
plt.plot(times, pops)
plt.show()
