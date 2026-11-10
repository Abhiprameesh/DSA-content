def find_max(arr, i):
    if i == len(arr) - 1:
        return arr[i]
    return max(arr[i], find_max(arr, i+1))
arr = [1, 2, 3, 4, 5]
print(find_max(arr, 0))