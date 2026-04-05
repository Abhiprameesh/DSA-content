def countFrequencies(nums):
    freq = {}

    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    result = []
    for key, value in freq.items():
        result.append([key, value])

    return result