#
# FireEvac.py - Fire Evacuation Simulation
# 

import matplotlib.pyplot as plt
import numpy as np
import random
from entities import *

##### Simulation Essentials #####

MaxRows = 100
MaxCols = 100

def Converter(row, col, limits):
    x = col
    y = limits[0] - row - 1
    return (x, y)

def scatterPlot(itemlist, colour, limits):
    xlist = []
    ylist = []
    slist = []
    for r,c in itemList:
        ylist.append(limits[0] - r -1)
        xlist.append(c)
        slist.append(200)
    plt.scatter(xlist,ylist,color=colour,marker='s', s=slist)

##### Preparing Entities for plotting #####

def scatterEmployees(employees, limits):
    xlist = []
    ylist = []
    slist = []
    clist = []
    for e in range(len(employees)):
        ylist.append(limits[0] - employees[e].getRow() - 1)
        xlist.append(employees[e].getCol())
        slist.append(100)
        clist.append(e)
    plt.scatter(xlist,ylist,s=slist,c=clist)

def scatterCEO(ceo, limits):
    xlist = []
    ylist = []
    slist = []
    clist = []
    for m in range(len(ceo)):
        ylist.append(limits[0] - ceo[m].getRow() - 1)
        xlist.append(ceo[m].getCol())
        slist.append(100)
        clist.append(m)
    plt.scatter(xlist,ylist,s=slist,c=clist)


def scatterFiremen(firemen, limits):
    xlist = []
    ylist = []
    slist = []
    clist = []
    for g in range(len(firemen)):
        ylist.append(limits[0] - firemen[g].getRow() - 1)
        xlist.append(firemen[g].getCol())
        slist.append(100)
        clist.append(g)
    plt.scatter(xlist,ylist,s=slist,c=clist)

##### Creating Fire #####

# Temperature reading that reads heat of fire, modelled in accordance to the heat of real life civilian fire temperatures
def temp(tempArray):
    tempReading = 0.1 * (tempArray.sum() + tempArray[1,1])
    return tempReading

def readFire(firePath):
    firePath = np.zeros((MaxRows,MaxCols))
    # Reading map from csv
    fireList = []
    fileobj = open('Fire.csv', 'r')
    for line in fileobj:
        SingleLine = line.strip()
        ints = [int(x) for x in SingleLine.split(',')]
        flist.append(ints)
    fileobj.close()

    fireArray = np.array(fireList)
    firePath = fireArray.copy()
    next = np.zeros((MaxRows,MaxCols))

    for time in range(25):
        for r in range(1, size-1):
            for c in range (1, size- 1 ):
                next [r,c] = temp(firePath[r-1:r+4,c-1:c+1])

        next = np.where(fireArray>next, fireArray, next)

        print(next)
        firePath = next.copy()
    return firePath

def main():

    # Map Limitations
    limits = [MaxRows, MaxCols]

    # Main Entrance/Exit Location

    door = [20,50]
    doorOpen = True

    # Employees Involved in Fire Evac
    employeeNames = ['Liam', 'John', 'Aaron', 'Sophie', 'Lily','Jordan']
    employeeNo = 5
    employeeList = []

    # CEO Involved in Fire Evac
    ceoName = ['Andrew']
    ceoNo = 1
    ceoList = []

    # Firemen Involved in Fire Evac
    firemenNames = ['Vulcan', 'Apollo', 'Sekhmet'] # Get the references?
    firemenNo = 3
    firemenList = []

    ## Adding entities to grid ##

    for em in range(employeeNo):
        employeeList.append(Employees(limits, employeeNames[em]))

    for c in range(ceoNo):
        ceoList.append(CEO(limits, ceoName[c]))

    for fm in range(firemenNo):
        firemenList.append(Fireman(limits, firemenNames[fm]))

    # Establishing Evac Sim

    for time in range(25):
        print('Run! The Building is burning!')
        print('#######')
        print('Building has been burning for', time, 'seconds')

        for emp in range(employeeNo):
            if doorOpen == True:
                employeeList[emp].escape(door, limits)
            plt.annotate(employeeList[emp].name,Converter(employeeList[emp].row,employeeList[emp].col,limits))

        for co in range(ceoNo):
            if doorOpen == True:
                ceoList[co].escape(door, limits)
            plt.annotate(ceoList[co].name,Converter(ceoList[co].row,ceoList[co].col,limits))

        for fr in range(firemenNo):
            if dooropen == True:
                firemenList[fr].FindSurvivors(door, limits)
            plt.annotate(firemenList[fr].name,Converter(firemenList[fr].row,firemenList[fr].col,limits))

## Establising when employees will push CEO
        if employeeList[emp].escape(door, limits) == ceoList[co].escape(door, limits):
            self.push == True and self.fall == True
## Establishing when employees get help from firemen
        if employeeList[emp].escape(door, limits) == firemenList[fr].FindSurvivors(door, limits):
            self.grabbed == True and self.grab == True
## Establishing when ceo gets help from firemen
        if ceoList[co].escape(door, limits) == firemenList[fr].FindSurvivors(door, limits):
            self.grabbed == True and self.grab == True

        scatterEmployees(employeeList, limits)
        scatterCEO(ceoList, limits)
        scatterFiremen(firemenList, limits)
        scatterPlot(door, 'green', limits)
        plt.xlabel('Fire Started Here')
        plt.ylabel('No Exit Here')
        plt.xlim(-1,MaxCols)
        plt.ylim(-1,MaxRows)
        plt.title('Run! The Building is on Fire!')
        plt.imshow(readFire(), cmap=plt.cm.hot)
        plt.colorbar()
        plt.pause(1)
        plt.clf()

if __name__ == '__main__':
    main()
