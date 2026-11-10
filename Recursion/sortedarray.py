def is_sorted(arr, n):
    if n == len(arr) - 1:
        return True
    if arr[n] > arr[n+1]:
        return False
    return is_sorted(arr, n+1)
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr, 0))