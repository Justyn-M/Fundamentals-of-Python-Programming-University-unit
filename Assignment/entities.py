#
# entities.py - characters involved in fire evacuation simulation
#
# Characters:
#          Firemen - Paid? guardians who are trying to save people
#          Employees - Paid workers trying to evacuate building
#          CEO - Company boss evacuating with Employees
#

import random

class Employees():
    def __init__(self, limits, name):
        self.row = random.randint(0, limits[0]-1)
        self.col = random.randint(0, limits[1]-1)
        self.name = name
        self.burned = False
        self.push = False
        self.escaped = False
        self.grabbed = False

    def escape(self, door, limits):   # Moore Neighborhood
        if self.burned == False and self.escape == False and self.grabbed == False:
            # walk up
            if random.randint(1,9) == 1:
                self.row = self.row + 1
                self.col = self.col
            # walk down
            elif random.randint(1,9) == 2:
                self.row = self.row - 1
                self.col = self.col
            # walk right
            elif random.randint(1,9) == 3:
                self.row = self.row
                self.col = self.col + 1
            # walk left
            elif random.randinit(1,9) == 4:
                self.row = self.row
                self.col = self.col - 1
            # walk North East
            elif random.randinit(1,9) == 5:
                self.row = self.row + 1
                self.col = self.col + 1
            # walk South West
            elif random.randinit(1,9) == 6:
                self.row = self.row -1
                self.col = self.col -1
            # walk North West
            elif random.randinit(1,9) == 7:
                self.row = self.row + 1
                self.col = self.col - 1
            # walk South East
            elif random.randinit(1,9) == 8:
                self.row = self.row - 1
                self.col = self.col + 1
            else:
            # stay stationery because character is thinking what to do
                self.row = self.row
                self.col = self.col

            # Entity has escaped
            if self.row == 20 and self.col == 50:
                self.escaped == True
                print(self.name, 'has escaped the fire')
            else:
                print(self.name, 'is still finding their way out')

            if self.grabbed == True:
                # walk up X 2 speed
                if random.randint(1,9) == 1:
                    self.row = self.row + 2
                    self.col = self.col
            # walk down X 2 Speed
                elif random.randint(1,9) == 2:
                    self.row = self.row - 2
                    self.col = self.col
            # walk right X 2 Speed
                elif random.randint(1,9) == 3:
                    self.row = self.row
                    self.col = self.col + 2
            # walk left X 2 Speed
                elif random.randinit(1,9) == 4:
                    self.row = self.row
                    self.col = self.col - 2
            # walk North East X 2 Speed
                elif random.randinit(1,9) == 5:
                    self.row = self.row + 2
                    self.col = self.col + 2
            # walk South West X 2 Speed
                elif random.randinit(1,9) == 6:
                    self.row = self.row - 2
                    self.col = self.col - 2
            # walk North West X 2 Speed
                elif random.randinit(1,9) == 7:
                    self.row = self.row + 2
                    self.col = self.col - 2
            # walk South East X 2 Speed
                elif random.randinit(1,9) == 8:
                    self.row = self.row - 2
                    self.col = self.col + 2
                else:
                    # stay stationery because character is thinking what to do
                    self.row = self.row
                    self.col = self.col

            if self.push == True:
                print(self.name, 'says: Andrew You dont pay me ENOUGH!')
                print(self.name, 'has pushed Andrew the CEO!')
            
            if self.burned == True:
                print(self.name, 'has burned in the fire')

            if self.row > 100:
                self.burned = True
                print(self.name, 'has passed out from the fumes')
            elif self.col > 100:
                self.burned = True
                print(self.name, 'has passed out from the fumes')
            elif self.row < 0:
                self.burned = True
                print(self.name, 'has passed out from the fumes')
            else:
                print(self.name, 'is still finding their way out')
class CEO():
    def __init__(self, limits, name):
        self.row = random.randint(0, limits[0]-1)
        self.col = random.randint(0, limits[1]-1)
        self.name = name
        self.burned = False
        self.escaped = False
        self.fall = False
        self.grabbed = False

    def escape(self, door, limits):
        if self.burned == False and self.escape == False and self.grabbed == False:
            # walk up
            if random.randint(1,9) == 1:
                self.row = self.row + 1
                self.col = self.col
            # walk down
            elif random.randint(1,9) == 2:
                self.row = self.row - 1
                self.col = self.col
            # walk right
            elif random.randint(1,9) == 3:
                self.row = self.row
                self.col = self.col + 1
            # walk left
            elif random.randinit(1,9) == 4:
                self.row = self.row
                self.col = self.col - 1
            # walk North East
            elif random.randinit(1,9) == 5:
                self.row = self.row + 1
                self.col = self.col + 1
            # walk South West
            elif random.randinit(1,9) == 6:
                self.row = self.row -1
                self.col = self.col -1
            # walk North West
            elif random.randinit(1,9) == 7:
                self.row = self.row + 1
                self.col = self.col - 1
            # walk South East
            elif random.randinit(1,9) == 8:
                self.row = self.row - 1
                self.col = self.col + 1
            else:
            # stay stationery because character is thinking what to do
                self.row = self.row
                self.col = self.col

            # Entity has escaped
            if self.row == 20 and self.col == 50:
                self.escaped == True
                print(self.name, 'has escaped the fire')
            else:
                print(self.name, 'is still finding their way out')

            if self.grabbed == True:
                # walk up X 2 speed
                if random.randint(1,9) == 1:
                    self.row = self.row + 2
                    self.col = self.col
            # walk down X 2 Speed
                elif random.randint(1,9) == 2:
                    self.row = self.row - 2
                    self.col = self.col
            # walk right X 2 Speed
                elif random.randint(1,9) == 3:
                    self.row = self.row
                    self.col = self.col + 2
            # walk left X 2 Speed
                elif random.randinit(1,9) == 4:
                    self.row = self.row
                    self.col = self.col - 2
            # walk North East X 2 Speed
                elif random.randinit(1,9) == 5:
                    self.row = self.row + 2
                    self.col = self.col + 2
            # walk South West X 2 Speed
                elif random.randinit(1,9) == 6:
                    self.row = self.row - 2
                    self.col = self.col - 2
            # walk North West X 2 Speed
                elif random.randinit(1,9) == 7:
                    self.row = self.row + 2
                    self.col = self.col - 2
            # walk South East X 2 Speed
                elif random.randinit(1,9) == 8:
                    self.row = self.row - 2
                    self.col = self.col + 2
                else:
                    # stay stationery because character is thinking what to do
                    self.row = self.row
                    self.col = self.col
            
            if self.fall == True:
               self.burned == True
               print('Andrew has been pushed by an employee!, he is now unconscious!')

            if self.burned == True:
                print(self.name, 'perished')

            if self.row > 100:
                self.burned = True
                print(self.name, 'has passed out from the fumes')
            elif self.col > 100:
                self.burned = True
                print(self.name, 'has passed out from the fumes')
            elif self.row < 0:
                self.burned = True
                print(self.name, 'has passed out from the fumes')
            else:
                print(self.name, 'is still finding their way out')

class Fireman():
    def __init__(self, limits, name):
        self.row = random.randint(0, limits[0]-1)
        self.col = random.randint(0, limits[1]-1)
        self.name = name
        self.grab = False

        # Firemen are immune to fire hence they don't get burned, they are not immune to the fire because they wear protection. Check the names of the firemen to understand why.

    def FindSurvivors(self, fire, limits): 
        if self.grab == False:
            if random.randint(1,9) == 1:
                self.row = self.row + 2
                self.col = self.col
            # walk down
            elif random.randint(1,9) == 2:
                self.row = self.row - 2
                self.col = self.col
            # walk right
            elif random.randint(1,9) == 3:
                self.row = self.row
                self.col = self.col + 2
            # walk left
            elif random.randinit(1,9) == 4:
                self.row = self.row
                self.col = self.col - 2
            # walk North East
            elif random.randinit(1,9) == 5:
                self.row = self.row + 2
                self.col = self.col + 2
            # walk South West
            elif random.randinit(1,9) == 6:
                self.row = self.row - 2
                self.col = self.col - 2
            # walk North West
            elif random.randinit(1,9) == 7:
                self.row = self.row + 2
                self.col = self.col - 2
            # walk South East
            elif random.randinit(1,9) == 8:
                self.row = self.row - 2
                self.col = self.col + 2
            else:
            # stay stationery because character is thinking what to do
                self.row = self.row
                self.col = self.col

            if self.grab == True:
                print(self.name, 'Grabs a Survivor and leads them out')

