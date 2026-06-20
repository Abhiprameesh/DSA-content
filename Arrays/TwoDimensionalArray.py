# Day 1 - 11, 15, 10, 6
# Day 2 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 15, 18, 14, 9

import numpy as np

twoDarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDarray)
#insert a new column at the start of the array
newTwoDArray = np.insert(twoDarray, 0, [[1,2,3,4]], axis=1)
print(newTwoDArray)
#insert a new row at the start of the array
newTwoDArray = np.insert(twoDarray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)

#traversal of 2 dimensional array
def traverse2DArray(twoDarray):
    for i in range(len(twoDarray)):
        for j in range(len(twoDarray[0])):
            print(twoDarray[i][j], end=" ")
            
traverse2DArray(twoDarray)