def partial_sort(arr, k):
    """Partially sorts an array to place the k smallest elements at the beginning."""

    if k <= 0 or k > len(arr):  
        return arr  

    for i in range(min(k, len(arr))):  
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  

    return " ".join(map(str, arr))  
n = int(input())
arr = list(map(int, input().split())) 

k = int(input())

sorted_arr_str = partial_sort(arr, k)
print(sorted_arr_str)
