import time

List = [i for i in range(10000)]
print(len(List))
s1time = time.time()

for element in List:
    print(element,end=" ")

print()
print(time.time() - s1time)

s2time = time.time()

for i in range(0,10000-1):
    print(List[i],end=" ")


print()
print(time.time() - s2time)