# leetcode 1200 Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/

'''
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

Constraints:
a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
'''

# My solution
# TimeComplexity: O(nlogn)
# Runtime: 60 ms, Memory: 31.23 MB
def minimumAbsDifference(arr):
    arr.sort()
    minDiff = float('inf')
    for i in range(1, len(arr)):
        minDiff = min(minDiff, arr[i] - arr[i - 1])
    res = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == minDiff:
            res.append([arr[i - 1], arr[i]])
    return res

# Test cases
arr = [4,2,1,3]
'''
Expected Output:
[[1,2],[2,3],[3,4]]
'''
print(minimumAbsDifference(arr))

arr = [1,3,6,10,15]
'''
Expected Output:
[[1,3]]
'''
print(minimumAbsDifference(arr))

arr = [3,8,-10,23,19,-4,-14,27]
'''
Expected Output:
[[-14,-10],[19,23],[23,27]]
'''
print(minimumAbsDifference(arr))

