#import numpy as np
import matplotlib.pyplot as plot
import time
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def insertion_sort_time(arr):
    start = time.time()
    insertion_sort(arr)
    end = time.time()
    return end - start

def list_timesort(arr):
    start = time.time()
    list.sort(arr)
    end = time.time()
    return end - start

def random_change(arr):
    differents = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) - 1):
            if arr[i] == arr[j]:
                differents += 1
    return differents

Numbers = []
Times = []
array = []

for i in range(10):
    N = (i + 1) * 100
    for i in range(N):
        array.append(random.randint(1, 100))
    Times.append(insertion_sort_time(array))
    Numbers.append(N)

print(random_change(array))
Numbers1 = []
Times1 = []
array = []
for i in range(10):
    N = (i + 1) * 100
    for i in range(N):
        array.append(random.randint(1, 100))
    Times1.append(insertion_sort_time(array))
    Numbers1.append(N)

print(random_change(array))
plot.plot(Numbers, Times, marker='o', color = 'g')
plot.plot(Numbers1, Times1, marker='o', color='r')
plot.show()
