from array import *

arr = array('i', [3, 1, 5, 4, 2, 100, 15, 45, 40])

for i in range(0, len(arr)):
    print(arr[i], end=' ')
print()


def insertionsort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = tmp


def mergesort(arr, a , b):
    if a < b:
        c = (a+b)/2
        print(c)
        print(a)
        print(b)
        mergesort(arr, a, c)
        mergesort(arr, c+1, b)





insertionsort(arr)
for i in range(0, len(arr)):
    print(arr[i], end=' ')

arra = array('i', [3, 1, 5, 4, 2, 24, 15, 55, 40])

mergesort(arra, 0, len(arra) - 1)
print()