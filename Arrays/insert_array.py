import array

my_array1 = array.array('i', [1,2,3,4])
print (my_array1)
my_array1.insert(2,6)
print(my_array1) 
#time complexity: O(n) because we may need to shift elements to the right to make space for the new element.
#space complexity: O(1) because we are inserting an element in place without using additional space.
