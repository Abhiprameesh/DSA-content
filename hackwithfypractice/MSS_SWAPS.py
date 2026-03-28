def kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_mss_with_k_swaps(n, k, arr):
    # Step 1: Sort array
    sorted_arr = sorted(arr)

    # Step 2: Try improving array using swaps
    # Copy original array
    improved = arr[:]

    # Replace smallest values with largest ones
    i = 0
    j = n - 1

    swaps = k
    while swaps > 0 and i < j:
        if improved[i] < improved[j]:
            improved[i], improved[j] = improved[j], improved[i]
            swaps -= 1
        i += 1
        j -= 1

    # Step 3: Find MSS
    return kadane(improved)


# Input
n = int(input())
k = int(input())
arr = [int(input()) for _ in range(n)]

print(max_mss_with_k_swaps(n, k, arr))