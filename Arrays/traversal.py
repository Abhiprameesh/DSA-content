from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3, 1.5, 1.6])

def traverseArray(array):
    for i in array:
        print(i)
traverseArray(arr1)
#time complexity: O(n) because we need to visit each element in the array once.
#space complexity: O(1) because we are using a constant amount of space to store the loop variable and the array reference.
#traversearray means to visit each element in the array and perform some operation on it. In this case, we are simply printing each element of the array.