#
# numbers3b.py: Read in a list of numbers (0 to exit) and give the sum of the numbers
#

count = 0
total = 0
print('Enter a list of numbers, zero  to exit ')
number = int(input())

while number !=  0:
    count = count + 1
    total = total + number
    print('Next number ')
    number = int(input())

print('Total is ', total, ' and count is ', count)

