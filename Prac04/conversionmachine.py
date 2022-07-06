#
# conversionmachine.py - converting between temperature formats
#

from conversions import *

print('\nConversions List\n')

converteds = []

choice = input('What would you like to do?: e(X)it, fahr2cel (f2c), cel2fahr (c2f) ')

while choice[0].upper() != 'X':
    if choice[0].upper() == 'f2c':
        print('\nSELECTED CONVERSION -- fahr2cel\n')
        testF = 'what you typed in'
        testC = fahr2cel(testF)
        print('Fahrenheit is', testF, 'Celsius is', testC)
        print()

    elif choice[0].upper() == 'c2f':
        print('\nSELECTED CONVERSION -- cel2fahr\n')
        testCel = 'what you typed in'
        testFahr = cel2fahr(testCel)
        print('Celsius is', testCel, 'Fahrenheit is', testFahr)
        print()
    else:
        print('Invalid selection.')
    choice = input('What would you like to do?: e(X)it, fahr2cel (f2c), cel2fahr (c2f)')

print('\nGOODBYE!\n')


