#
# Author : 
# ID : 
#
# shrimp.py - Class definitions for simulation of brine shrimp 
#
# Revisions: 
#
# 2/10/2019 – Base version for assignment
#


class Shrimp():
    time2hatch = 4
    states = ["egg","adult"]
    
    def __init__(self, pos):
        self.pos = pos
        self.state = self.states[0]
        self.age = 0
        
    def __str__(self):
        return self.state + " @ " + str(self.pos)
    
    def stepChange(self):
        self.age += 1
        if self.state == "egg":
            self.pos[1] -= 10
            if self.age > self.time2hatch:
                self.state = "adult"
        else:
            xmov = 10
            ymov = 10
            self.pos[0] += xmov
            self.pos[1] += ymov
                        
    def getSize(m):
        if m.state == "egg":
            size = 5
        else:
            size = 15
        return size