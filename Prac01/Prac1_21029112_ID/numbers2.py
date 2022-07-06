#
# numbers2.py: Read in 10 numbers and give sum of numbers
#

print('Enter 10 numbers ')
total = 0
for i in range(10):
    print('Enter a number (', i, ') ')
    number = int(input())
    total = total + number

print('Total is ', total)

