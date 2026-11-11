def is_sorted(arr, i ):
    if i == len(arr) - 1:
        return True 
    if arr[i] > arr[i+1]:
        return False
    return is_sorted(arr, i + 1)
arr = [1, 2, 3, 4, 5]
print(is_sorted(arr, 0))