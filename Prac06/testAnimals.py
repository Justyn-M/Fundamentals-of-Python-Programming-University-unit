#
# testCat.py - testing Cat class
#

from animals import Cat, Dog, Bird

garfield = Cat('Garfield', '1/1/1978', 'Orange', 'Tabby')

garfield.printit()

print(garfield)

snoopy = Dog('Snoopy', '4/8/1950', 'White and Black', 'Beagle')

snoopy.printit()

print(snoopy)

woodstock = Bird('Woodstock', '4/3/1966', 'Yellow', 'Canary')

woodstock.printit()

print(woodstock)

