#
# Author : 
# ID : 
#
# yebbleLife_base.py - Basic simulation of wildlife
#
# Revisions: 
#
# 12/4/21 – Base version for assignment
#

import random
import matplotlib.pyplot as plt
import numpy as np

RMAX  = 20
CMAX  = 30
POP   = 20
STEPS = 10
    
def main():

    print("\n ### 2D Growth Simulation ###\n")
    
    # Initialise population

    popgrid = np.zeros((RMAX, CMAX), dtype=int)
    nextgrid = np.zeros((RMAX, CMAX), dtype=int)
    
    for i in range(POP):
        randR = random.randint(0,RMAX-1)
        randC = random.randint(0,CMAX-1)
        popgrid[randR,randC] += 1
        print("Life at : [", randR, randC, "]")

    print("\n ### INITIAL POPULATION ###")
    
    plt.imshow(popgrid)   # Note plt origin is top left 
    plt.show()

    # Simulation
    
    for i in range(STEPS):
        print("\n ### TIMESTEP ",i, "###")

    # Move population - by one step (randomly) in x and y
        
        nextgrid = np.zeros((RMAX, CMAX), dtype=int)

        for r in range(RMAX):
            for c in range(CMAX):
                for i in range(popgrid[r,c]):
                    rmoved = r + random.choice([-1,0,1])
                    cmoved = c + random.choice([-1,0,1])
                    if rmoved == -1:
                        rmoved = 0
                    if cmoved == -1:
                        cmoved = 0
                    if rmoved == RMAX:
                        rmoved = RMAX - 1
                    if cmoved == CMAX:
                        cmoved = CMAX -1                     
                    nextgrid[rmoved,cmoved] += 1

    # Reproduction - 10% chance of reproducing +1 to pop in cell
    
        for r in range(RMAX):
            for c in range(CMAX):
                for i in range(nextgrid[r,c]):
                    if random.random() <= 0.1:
                        nextgrid[r,c] += 1
                        
    # Update grid
                        
        popgrid = nextgrid

    # Plot current population as array (could also use scatter plot)
    
        plt.imshow(popgrid)   # Note plt origin is top left 
        plt.show()
    
if __name__ == "__main__":
    main()
