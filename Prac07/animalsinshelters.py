#
# animalsinshelters.py - classes for animals and pet shelter
#

class Animal():
    myclass = 'Animal'

    def __init__(self, name, dob, colour, breed):
        self.name = name
        self.dob = dob
        self.colour = colour
        self.breed = breed

    def __str__(self):
        return(self.name + '|' + self.dob + '|' + self.colour + '|' + self.breed)

    def priniit(self):
        spacing = 5 - len(self.myclass)
        print(self.myclass.upper(), spacing*'' + ':', self.name, '\tDOB: ', self.dob, '\tColour:', self.colour, '\tBrred: ', self.breed)

class Dog(Animal):
    myclass = 'Dog'

class Cat(Animal):
    myclass = 'Cat'

class Bird(Animal):
    myclass = 'Bird'

class Shelter():
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.processing = []
        self.available = []
        self.adopted = []

    def displayProcessing(self):
        print('Current processing list:')
        for a in self.processing:
            a.printit()
            #print()

    def displayAvailable(self):
        print('Current available list:')
        for a in self.available:
            a.printit()
            #print()

    def displayAdopted(self):
        print('Current adopted list:')
        for a in self.adopted:
            a.printit()
            #print()

    def displayAll(self):
        self.displayProcessing()
        self.displayAvailable()
        self.displayAdopted()

    def newAnimal(self, atype, name, dob, colour, breed):
        temp = None
        if atype == 'Dog':
            temp = Dog(name, dob, colour, breed)
        elif atype == 'Cat':
            temp = Cat(name, dob, colour, breed)
        elif atype == 'Bird':
            temp = Bird(name, dob, colour, breed)
        else:
            print('Error, unknown animal type: ', atype)
        if temp:
           self.processing.append(temp)
           print('Added', name, 'to processing list')
           

    def makeAvailable(self, name):
        temp = None
        index = 0
        while not temp and index < len(self.processing):
            print('Checking element', index)
            if self.processing[index].name == name:
                temp = self.processing[index]
            index += 1
        if temp:
            self.processing.remove(temp)
            self.available.append(temp)
            print(name, 'moved from processing to available')
        else:
            print('Animal not found:', name)

    def makeAdopted(self, name):
        temp = None
        index = 0
        while not temp and index < len(self.available):
            print('Checking element', index)
            if self.available[index].name == name:
                temp = self.available[index]
            index += 1
        if temp:
            self.available.remove(temp)
            self.adopted.append(temp)
            print(name, 'moved from available to adopted')
        else:
            print('Animal not found:', name)

