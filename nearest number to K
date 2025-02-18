def find_closest_element(arr, k):
    # Initialize variables
    closest_value = arr[0]
    min_distance = abs(arr[0] - k)
    
    # Iterate through the array
    for num in arr:
        current_distance = abs(num - k)
        
        # Update closest_value and min_distance if a closer element is found
        if current_distance < min_distance:
            min_distance = current_distance
            closest_value = num
        # If the distance is equal, choose the smaller element
        elif current_distance == min_distance:
            if num < closest_value:
                closest_value = num
    
    return closest_value

# Input reading
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

# Find and print the closest element
result = find_closest_element(arr, k)
print(result)
