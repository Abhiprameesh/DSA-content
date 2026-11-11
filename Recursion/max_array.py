def max_array(arr, i):
    if i == len(arr) - 1:
        return arr[i]
    return max(arr[i], max_array(arr, i + 1))
arr = [1, 2, 3, 4, 5]
print(max_array(arr, 0))