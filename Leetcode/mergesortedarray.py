nums1 = [1, 2, 3, 0, 0 , 0]
nums2 = [2, 5, 6]
m = 3
n = 3

right = m + n - 1
while n > 0:
    if m > 0 and nums1[m-1] > nums2[n-1]:
        nums1[right] = nums1[m-1]
        m -= 1
    else:
        nums1[right] = nums2[n-1]
        n-=1
    right -= 1