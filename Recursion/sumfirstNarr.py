def array_sum(arr, n):
    if n == len(arr):
        return 0
    return arr[i] + array_sum(arr, n+1)
arr = [1, 2, 3, 4, 5]
print(array_sum(arr, 0))