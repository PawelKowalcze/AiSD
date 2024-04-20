import time
from random import *

def insertionsort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = tmp


#def merge(arra, a, c, b)


def mergesort(arr):
    if len(arr) > 1:
        left_array = arr[:len(arr)//2]
        right_array = arr[len(arr)//2:]


        mergesort(left_array)
        mergesort(right_array)

        #print(left_array)
        #print(right_array)

        #merge
        i = 0 # index of left array
        j = 0 # index of right array
        k = 0 # index of whole array
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1

            else:
                arr[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1


timearr = []
stime = time.time()
for a in range(1000):
    print(a)
    a += 1
    arr = []
    itertime = time.time()
    for b in range(500):
        arr.append(randint(0,999))
    insertionsort(arr)
    timearr.append(time.time() - itertime)
print('Sredni czas ', sum(timearr)/len(timearr))
print('Najwolniejszy czas: ' + str(max(timearr)))
print('Najszybszy czas: ' + str(min(timearr)))
print('Całkowity czas wykonania funkcji insertionsort: ' + str(time.time() - stime))


timearr = []
stime2 = time.time()
for a in range(1000):
    print(a)
    a += 1
    arr = []

    itertime = time.time()
    for b in range(500):
        arr.append(randint(0,999))
    mergesort(arr)
    timearr.append(time.time()- itertime)
print('Sredni czas ', sum(timearr)/len(timearr))
print('Najwolniejszy czas: ' + str(max(timearr)))
print('Najszybszy czas: ' + str(min(timearr)))
print('Całkowity czas wykonania funkcji mergesort: ' + str(time.time() - stime2))