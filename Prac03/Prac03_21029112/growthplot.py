#
# growthplot.py - plotting a graph of a simulation of unconstrained growth
#

import matplotlib.pyplot as plt

print("\nSIMULATION - Unconstrianed Growth\n")

length = 100
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

print('Time: ', 100, ' \tGrowth: ', 0, ' \tPopulation: ', 100)
times =[0]
pops=[100]

for i in range(1, int(num_iter) + 1 ):
    growth = growth_step * population
    population = population + growth
    time = i * time_step
    times.append(time)
    pops.append(population)
    print('Time: ', time, ' \tGrowth: ', growth, ' \tPopulation: ', population)

print('\nPROCESSING COMPLETE.\n')

plt.title('Prac 3.1: Unconstrained Growth')
plt.plot(times, pops, color = 'red')
plt.show()
