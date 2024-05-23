from math import *

map = open('TSP.txt', 'r')
coordinates = map.read()
lines = list(coordinates.split('\n'))
data =[]

for line in lines:
    data.extend(line.split('\t'))
print(data)
## 1 --> 0 2-->3 3-->6 4-->9 5-->12
startingCity = 2
start = startingCity
#print((len(data)-1)/3)
for i in range(startingCity + 2, int((len(data)-1))):
    if i%3 == 0:
        print(i, 'i')
        squares1 = (float(data[i-2]) - float(data[i + 1])) ** 2
        squares2 = (float(data[i-1]) - float(data[i + 2])) ** 2
        distance = sqrt(squares1 + squares2)
        print('Distance between ', data[i-3], ' and ', data[i], ' is ', distance)
        if startingCity != 1:
            for i in range(3, startingCity+i+2):
                print(i, 'i')
                squares1 = (float(data[i - 2]) - float(data[i + 1])) ** 2
                squares2 = (float(data[i - 1]) - float(data[i + 2])) ** 2
                distance = sqrt(squares1 + squares2)
                print('Distance between ', data[i - 3], ' and ', data[i], ' is ', distance)