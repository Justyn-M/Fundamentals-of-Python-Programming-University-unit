#
# animalFile.py - Even more animals!
#

from animals import Cat, Dog, Bird

myanimals = []

afile = open('animals.csv', 'r')

aline = afile.readline()

while aline:
    splitline = aline.split(',')
    #print(splitline)
    temp = None
    if splitline[0] == 'Dog':
        temp = Dog(splitline[1], splitline[2], splitline[3], splitline[4].strip())
    elif splitline[0] == 'Cat':
        temp = Cat(splitline[1], splitline[2], splitline[3], splitline[4].strip())
    elif splitline[0] == 'Bird':
        temp = Bird(splitline[1], splitline[2], splitline[3], splitline[4].strip())
    else:
        print('Unrecognised Animal', splitline[0])

    if temp:
        myanimals.append(temp)
    aline = afile.readline()

afile.close()

for a in myanimals:
    a.printit()
    print()

