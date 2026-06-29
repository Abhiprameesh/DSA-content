# to find the missing number in a integer array of 1 to n numbers
def missing_number(arr, n):
    total = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total - arr_sum
print("Enter the upper limit (n) of the sequence 1 to n: ")
n = int(input())
print("Enter the elements of the array (space-separated): ")
arr = list(map(int, input().split()))
print("The missing number is:", missing_number(arr, n))
