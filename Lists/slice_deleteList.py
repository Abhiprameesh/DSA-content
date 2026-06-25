myList = ['a', 'b', 'c', 'd', 'e', 'f']

print(myList[1:4])  # Output: ['b', 'c', 'd']
myList.pop()  # Removes the element at index 2 ('c')
print(myList)  # Output: ['a', 'b', 'd', 'e', 'f']

del myList[1:3]  # Deletes elements from index 1 to 2 ('b' and 'd')
print(myList)  # Output: ['a', 'e', 'f']

myList.remove('e')  # Removes the first occurrence of 'e'
print(myList)  # Output: ['a', 'f']