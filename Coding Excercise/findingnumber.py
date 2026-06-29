import numpy as np

myarray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def find_number(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(i)

find_number(myarray, 21)