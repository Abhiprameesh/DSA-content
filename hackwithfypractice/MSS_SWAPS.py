def max_mss_with_k_swaps(n, k, arr):
    max_sum = float('-inf')

    # Try all possible subarrays
    for i in range(n):
        current = []
        
        for j in range(i, n):
            current.append(arr[j])

            # Step 1: Sort inside subarray (ascending)
            inside = sorted(current)

            # Step 2: Elements outside subarray (descending)
            outside = sorted(arr[:i] + arr[j+1:], reverse=True)

            # Step 3: Perform at most k swaps
            swaps = k
            idx_in = 0
            idx_out = 0

            while swaps > 0 and idx_in < len(inside) and idx_out < len(outside):
                if inside[idx_in] < outside[idx_out]:
                    inside[idx_in], outside[idx_out] = outside[idx_out], inside[idx_in]
                    swaps -= 1
                    idx_in += 1
                    idx_out += 1
                else:
                    break

            # Step 4: Compute sum
            current_sum = sum(inside)

            # Step 5: Update max
            max_sum = max(max_sum, current_sum)

    return max_sum


# -------- INPUT --------
n = int(input())
k = int(input())
arr = [int(input()) for _ in range(n)]

# -------- OUTPUT --------
print(max_mss_with_k_swaps(n, k, arr))