#
# people.py - class definitions for person, staff, student, etc
#

class Address():
    def __init__(self, number, street, suburb, postcode):
        self.number = number
        self.street = street
        self.suburb = suburb
        self.postcode = postcode

    def __str__(self):
        return(self.number + '' + self.street + ',' + self.suburb + ',' + self.postcode)

class Person():
    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address

    def displayPerson(self):
        print('Name:', self.name, '\tDOB:', self.dob)
        print('      Address:', str(self.address))

class Staff(Person):
    myclass = 'Staff'

    def __init__(self, name, dob, address, sid):
        super().__init__(name, dob, address)
        self.id = sid

    def displayPerson(self):
        super().displayPerson()
        print('      StaffID:', self.id)

class Student(Person):
    myclass = 'Student'

    def __init__(self, name, dob, address, sid):
        super().__init__(name, dob, address)
        self.id = sid

    def displayPerson(self):
        super().displayPerson()

class Undergraduate(Student):
    myclass = 'Undergraduate'

    def __init__(self, name, dob, address, sid):
        super().__init__(name, dob, address, sid)   

    def displayPerson(self):
        super().displayPerson()
        print('      UndergraduateStudentID:', self.id)

class Postgraduate(Student):
    myclass = 'Postgraduate'

    def __init__(self, name, dob, address, sid):
        super().__init__(name, dob, address, sid)

    def displayPerson(self):
        super().displayPerson()
        print('      PostgraduateStudentID:', self.id)


