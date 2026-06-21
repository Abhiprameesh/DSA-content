import numpy as np

#deletion of a column from 2D array
twoDarray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDarray)

newTwoDArray = np.delete(twoDarray, 0, axis=1)
print(newTwoDArray)