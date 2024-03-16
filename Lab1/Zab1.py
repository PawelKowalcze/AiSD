import statistics as stat
import time

stime = time.time()
L = [1,2]
s = 0
NumOfSameVal = 0

for i in range(2,48):
    y = L[i-1] + L[i-2]
    x = L[i-1] - L[i-2]
    L.append(y/x)

print("Lista:", L)


for element in L:
    s += element

print("Średnia: ", s/48)
print("Moda: ", stat.mode(L))

for element in L:
    if L.count(element) > 1:
        print(element, L.count(element))
        NumOfSameVal += 1

if NumOfSameVal == 0:
    print("Każda wartość pojawiła się tylko raz")


print(time.time() - stime)
