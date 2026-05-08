n = 6

arr = [9,46,24,52,20,13]

for i in range(n):

    # Assume current index has minimum element
    min_index = i

    # Find actual minimum element
    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    # Swap smallest element with current position
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(*arr)