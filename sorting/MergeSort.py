def merge(left, right):

    result = []

    i = 0
    j = 0

    # Compare elements from both arrays
    while i < len(left) and j < len(right):

        if left[i] < right[j]:

            result.append(left[i])

            i += 1

        else:

            result.append(right[j])

            j += 1

    # Add remaining elements
    while i < len(left):

        result.append(left[i])

        i += 1

    while j < len(right):

        result.append(right[j])

        j += 1

    return result


def merge_sort(arr):

    # Base condition
    if len(arr) <= 1:
        return arr

    # Find middle
    mid = len(arr) // 2

    # Divide array
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge sorted halves
    return merge(left, right)


n = int(input())

arr = list(map(int, input().split()))

sorted_arr = merge_sort(arr)

print(*sorted_arr)