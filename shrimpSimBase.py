#
# Author : 
# ID : 
#
# shrimpSimBase.py - Basic simulation of brine shrimp for assignment, S2 2019. 
#
# Revisions: 
#
# 2/10/2019 – Base version for assignment
#

import random
import matplotlib.pyplot as plt
import numpy as np
import time
from shrimp import Shrimp

XMAX = 1000
YMAX = 500
    
def main():
    monkeys = []
    
    for i in range(20):
        randX = random.randint(0,XMAX)
        randY = random.randint(0,YMAX)
        monkeys.append(Shrimp([randX,randY]))
        #print(monkeys[i])
     
    for i in range(10):
        print("\n ### TIMESTEP ",i, "###")
        xvalues = []
        yvalues = []
        sizes = []
        for m in monkeys:
            m.stepChange()
            #print(m)
            xvalues.append(m.pos[0])
            yvalues.append(m.pos[1])
            sizes.append(m.getSize())
        
        plt.scatter(xvalues, yvalues, s=sizes)   # Note plt origin is bottom left 
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        plt.show()
        time.sleep(2)
    
if __name__ == "__main__":
    main()