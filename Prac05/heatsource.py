#
# Name : Justyn Mahen
# ID   : 21029112
#
# heatsource.py - heat diffusion simulation
#
import numpy as np
import matplotlib.pyplot as plt

def calcheat(subarray):
    result = 0.1 * (subarray.sum() + subarray[1,1])
    return result

size = 10 

curr = np.zeros((size,size)) 
print(curr)

# create heat
hlist = []
fileobj = open('heatsource.csv', 'r')
for line in fileobj:
    line_s = line.strip()
    ints = [int(x) for x in line_s.split(',')]
    hlist.append(ints)
fileobj.close()

harray = np.array(hlist)
curr = harray.copy()
next = np.zeros((size,size)) 

for timestep in range(5): 
    for r in range(1, size-1): 
        for c in range (1, size- 1 ): 
            next [r,c] = calcheat(curr[r-1:r+2,c-1:c+2])
 
    next = np.where(harray>next, harray, next)

    print("Time step: ", timestep) 
    print(next)    
    curr = next.copy() 

    plt.imshow(curr, cmap=plt.cm.hot) 
    plt.show() 
