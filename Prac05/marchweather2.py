#
# marchweather2.py - Print march weather
#

import matplotlib.pyplot as plt

fileobj = open('marchweatherfull.csv')
data = fileobj.readlines()
fileobj.close()

mins = []
maxs = []
nines = []
threes = []

for line in data:
    splitline = line.strip().split(',')
    mins.append(float(splitline[2]))
    maxs.append(float(splitline[3]))
    nines.append(float(splitline[10]))
    threes.append(float(splitline[16]))

dates = [d for d in range(1,32)]
plt.plot(dates, mins, dates, maxs, dates, nines, dates, threes)
plt.title('March Weather')

plot.show()

file2 = open('marchout.csv', 'w')
for i in range (len(mins)):
    file2.write(str(mins[i]) + ',' + str(maxs[i]) + ',' + str(nines[i]) + ',' + str(threes[i]) + "\n")
file2.close()


