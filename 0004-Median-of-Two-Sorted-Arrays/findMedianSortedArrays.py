# leetcode 4 Median of Two Sorted Arrays
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6
'''

# My Solution: Brute Force
# Time Complexity: O((m + n)log(m, n))
# Runtime: 0 ms, Memory: 17.84 MB
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    sorted_nums = sorted(nums1 + nums2)
    if len(sorted_nums) % 2 == 0:
        return (sorted_nums[len(sorted_nums) // 2] + sorted_nums[len(sorted_nums) // 2 - 1]) / 2

    return sorted_nums[len(nums1 + nums2) // 2]

# Better Solution: Binary Search
# Time Complexity: O(log(m + n))
# Runtime: 0 ms, Memory: 18.21 MB
def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1)>len(nums2):
        nums1,nums2=nums2,nums1
    m=len(nums1)
    n=len(nums2)
    l=0
    h=m

    while l<=h:
        mid=(l+h)//2
        num1Part=mid
        num2Part=(m+n+1)//2-num1Part
        if num1Part==0:
            left1=float('-inf')
        else:
            left1=nums1[num1Part - 1]
        if num1Part==m:
            right1=float('inf')
        else:
            right1=nums1[num1Part]
        if num2Part==0:
            left2=float('-inf')
        else:
            left2=nums2[num2Part-1]

        if num2Part==n:
            right2=float('inf')
        else:
            right2=nums2[num2Part]
        if left1<=right2 and left2<=right1:
            if (m+n)%2==0:
                left_max =max(left1, left2)
                right_min =min(right1, right2)
                median=(left_max+right_min)/2
                return median
            else:
                median= max(left1,left2)
                return median
        if left1>right2:
            h=mid - 1
        else:
            l=mid + 1

# Test Case
nums1 = [1,3]
nums2 = [2]

# Explanation: merged array = [1,2,3] and median is 2.
output = 2
assert findMedianSortedArrays(nums1, nums2) == output

nums1 = [1,2]
nums2 = [3,4]

# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
output = 2.5
assert findMedianSortedArrays(nums1, nums2) == output

print("All test cases passed")
