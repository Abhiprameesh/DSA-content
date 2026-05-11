def bubble_sort(arr):
    n = len(arr)
    swap_count = 0
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1
    return arr, swap_count


n = int(input()) # Number of elements in array
arr = list(map(int, input().split())) # Array elements

sorted_arr, swaps = bubble_sort(arr)


print(" ".join(map(str, sorted_arr)))
print(swaps)
