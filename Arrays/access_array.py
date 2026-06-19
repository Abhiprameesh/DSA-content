from array import *
from operator import index
arr1 = array('i', [1,2,3,4,5,6])
def accessElement(array, index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])
        
accessElement(arr1, 8)
#accessing an array element with an index that is out of range will raise an IndexError. To avoid this, we can check if the index is within the valid range before accessing the element.
#time complexity: O(1) because we are accessing a specific index directly without needing to traverse the array.
#space complexity: O(1) because we are using a constant amount of space to store the index and the array reference.