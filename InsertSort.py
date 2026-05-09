def insertion_sort(arr):

    n = len(arr)

    for i in range(1, n):

        # Current element to insert
        key = arr[i]

        # Compare with previous elements
        j = i - 1

        # Shift larger elements to right
        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        # Insert key at correct position
        arr[j + 1] = key

    return arr


n = int(input())

arr = list(map(int, input().split()))

sorted_arr = insertion_sort(arr)

print(*sorted_arr)