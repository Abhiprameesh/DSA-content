from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr1.remove(4)
print (arr1)
#time complexity: O(n) because in the worst case, we may need to check each element in the array once to find the element to remove.
#space complexity: O(1) because we are using a constant amount of space to store the loop variable and the target value.
#logic behind the code: The code creates an array of integers and removes the element '4' from it using the remove() method. The updated array is then printed to the console.