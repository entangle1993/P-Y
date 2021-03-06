def findMedianSortedArrays(nums1, nums2) -> float:   #简单粗暴的中位数
    nums3 = sorted(nums1+nums2)  #sort()好像比sorted要快
    p = len(nums3)  #sorted：
    mid = p//2
    #print(mid)
    if p%2 ==0:
        #print('偶数')
        return (nums3[mid]+nums3[mid-1])/2
    else:
        return nums3[mid]

#print(findMedianSortedArrays([1,5],[2,4]))


def findMedianSortedArrays2(nums1, nums2) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    if n1 > n2:
        return findMedianSortedArrays2(nums2, nums1)
    k = (n1 + n2 + 1) // 2
    left = 0
    right = n1
    while left < right:
        m1 = left + (right - left) // 2
        m2 = k - m1
        if nums1[m1] < nums2[m2 - 1]:
            left = m1 + 1
        else:
            right = m1
    m1 = left
    m2 = k - m1
    c1 = max(nums1[m1 - 1] if m1 > 0 else float("-inf"), nums2[m2 - 1] if m2 > 0 else float("-inf"))
    if (n1 + n2) % 2 == 1:
        return c1
    c2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 < n2 else float("inf"))
    return (c1 + c2) / 2

print(findMedianSortedArrays2([1,3],[2,4]))

