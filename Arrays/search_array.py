import array
my_array1 = array.array('i', [1,2,3,4,5])
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search(my_array1, 3))  # Output: 2
print(linear_search(my_array1, 6))  # Output: -1
#time complexity: O(n) because in the worst case, we may need to check each element in the array once.
#space complexity: O(1) because we are using a constant amount of space to store the loop variable and the target value.