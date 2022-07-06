#
# conversions.py - module with functions to convert between units
#
#      fahr2cel : Convert from Fahrenheit to Celsius
#

def main():
    print('\nTesting textfun.py ')
    choice = input('Choose between f2c and c2f: ')
    if choice[0].upper == 'f2c':
        return fahr2cel
    elif choice[0].upper == 'c2f':
        return cel2fahr
    else:
        print('\nInvalid Selection.\n')

def fahr2cel(fahr):
    fahr = int(input('Enter Temperature in Fahrenheit: '))
    celsius = (fahr - 32) * (5/9)
    return celsius

def cel2fahr(cel):
    cel = int(input('Enter Temperature in Celsius: '))
    fahrenheit = (cel*9/5) + 32
    return fahrenheit

if __name__ == '__main__':
    main()

