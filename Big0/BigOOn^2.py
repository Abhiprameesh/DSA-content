def print_items(n):
    for i in range(n): 
        for j in range(n):
            print(i, j)
# The time complexity of this function is O(n^2) because it has a nested loop that iterates n times for each iteration of the outer loop, resulting in n * n = n^2 operations.