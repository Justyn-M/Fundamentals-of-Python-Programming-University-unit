#
# Author : 
# ID : 
#
# pasciroExample.py - Basic simulation of PaSciRo lifeforms for assignment, S2 2020. 
#
# Revisions: 
#
# 22/9/2019 – Base version for assignment
#

import random
import matplotlib.pyplot as plt
import numpy as np
import time

def stepChange(lifeform):
    if lifeform[2] == 1:
        lifeform[0] = lifeform[0] + random.randint(-3, 3)
        lifeform[1] = lifeform[1] + random.randint(-3, 3)


XMAX  = 200
YMAX  = 100
POP   = 20
STEPS = 10
    
def main():
    lifeforms = np.zeros((POP, 3), dtype=int)
    
    for i in range(POP):
        randX = random.randint(0,XMAX)
        randY = random.randint(0,YMAX)
        randTYPE = random.randint(0,2)
        lifeforms[i,0] = randX
        lifeforms[i,1] = randY
        lifeforms[i,2] = randTYPE
        print(lifeforms[i])
     
    for i in range(STEPS):
        print("\n ### TIMESTEP ",i, "###")
        xvalues = []
        yvalues = []
        colours = []
        for l in lifeforms:
            stepChange(l)
            #print(l)
            xvalues.append(l[0])
            yvalues.append(l[1])
            colours.append(l[2])
        
        plt.scatter(xvalues, yvalues, c=colours)   # Note plt origin is bottom left 
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        plt.show()
        time.sleep(2)
    
if __name__ == "__main__":
    main()
