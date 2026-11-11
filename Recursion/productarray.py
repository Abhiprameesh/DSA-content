def product_array(arr, i):
    if i == len(arr) - 1:
        return len(arr)
    return arr[i] * product_array(arr, i + 1)
arr = [1, 2, 3, 4, 5]  
print(product_array(arr, 0))