#
# shelters.py - testing pets and shelters class
#

from animalsinshelters import Dog, Cat, Bird, Shelter

print('\n#### Pet Shelter Program ####\n')

rspca = Shelter('RSPCA', 'Serpetine Meander', '123456')

rspca.newAnimal('Dog', 'Dude', '1/1/2011', 'Brown', 'Jack Russell')
rspca.newAnimal('Dog', 'Brutus', '1/1/1982', 'Brown', 'Rhodesian Ridgeback')
rspca.newAnimal('Cat', 'Oogie', '1/1/2006', 'Grey', 'Fluffy')
rspca.newAnimal('Bird', 'Big Bird', '10/11/1969', 'Yellow', 'Canary')
rspca.newAnimal('Bird', 'Dead Parrot', '1/1/2011', 'Dead', 'Parrot')

print('\nAnimals Added\n')

print('Listing Animals For Processing...\n')

rspca.displayProcessing()

# THis code is commented out until you have implemented
# the methods in animals.py

print('Processing animals...\n')

rspca.makeAvailable('Dude')
rspca.makeAvailable('Oogie')
rspca.makeAvailable('Big Bird')
rspca.makeAvailable('Goofy')

rspca.makeAdopted('Oogie')
rspca.makeAdopted('Goofy')

print('\nPrinting Updated List...\n')

rspca.displayAll()
