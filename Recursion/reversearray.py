
def reverse_recursive(arr, i, j):
    # Base Case: If pointers meet or cross, we are done
    if i >= j:
        return
    
    # Swap elements at the current pointers
    arr[i], arr[j] = arr[j], arr[i]
    
    # Recursive Call: Move pointers inward
    reverse_recursive(arr, i + 1, j - 1)

# Usage
arr1 = list(map(int, input().split()))
reverse_recursive(arr1, 0, len(arr1) - 1)
print(f"Output 1: {arr1}")