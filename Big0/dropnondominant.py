def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)
print_items(5)
# The time complexity of this function is O(n^2) because the nested loops dominate the time complexity. The first part of the function has a time complexity of O(n^2) due to the nested loops, while the second part has a time complexity of O(n). However, since O(n^2) grows faster than O(n), the overall time complexity is O(n^2).   