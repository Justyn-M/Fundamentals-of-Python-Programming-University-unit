#
# strings2.py: Read in a string and print it forwards  using a loop and a method call
#

instring = input('Enter a string ').upper()*2

# fowards  with a while loop

print('Forward string is: ', end='')
index = 1
while index < len(instring):
    print(instring[index], end='')
    index = index + 2
print()

# forwards  with a range loop

print('Forward string is: ', end='')
for index in range(1,len(instring),2):
    print(instring[index], end='')
print()

# forwards  with slicing

print('Forward string is:', instring[1::2])

