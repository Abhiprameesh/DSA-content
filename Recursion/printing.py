def print_array(arr, n):
    if n == len(arr):
        return
    print(arr[n])

    print_array(arr, n + 1)
arr = [1, 2, 3, 4, 5]
print_array(arr, 0)