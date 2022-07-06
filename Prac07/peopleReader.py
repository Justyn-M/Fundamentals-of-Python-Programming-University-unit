#
# peopleReader.py - read in people from file and create objects
#

from people import *

plist = []

with open('people.csv') as f:
    inpeople = f.readlines()

for inperson in inpeople:
    temp = None
    splitline = inperson.split(':')
    if splitline[0] == 'Staff':
        temp = Staff(splitline[1], splitline[2], splitline[3], splitline[4].strip())
    elif splitline[0] == 'Undergraduate':
        temp = Undergraduate(splitline[1], splitline[2], splitline[3], splitline[4].strip())
    elif splitline[0] == 'Postgraduate':
        temp = Postgraduate(splitline[1], splitline[2], splitline[3], splitline[4].strip())
    if temp:
        plist.append(temp)

for p in plist:
    p.displayPerson()


