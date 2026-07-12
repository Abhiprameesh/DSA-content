#Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
def pair_sum(arr, target):
    pairs = []# Initialize an empty list called result to store the pairs that add up to the target sum.
    for i in range(len(arr)):# Loop through each element in the array using its index.
        for j in range(i + 1, len(arr)):# Loop through the elements that come after the current element to avoid commutative pairs.
            if arr[i] + arr[j] == target:# Check if the sum of the current pair of elements is equal to the target sum.
                pairs.append((arr[i], arr[j]))# If the condition is met, append the pair as a tuple to the pairs list.
    return pairs #
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
result = pair_sum(arr, target)