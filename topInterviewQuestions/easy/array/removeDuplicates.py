# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

### Remove Duplicates from Sorted Array

'''
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k.
After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. 
The remaining elements beyond index k - 1 can be ignored.

Constraints:

1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''

# Solution
def removeDuplicates(nums: list[int]) -> int:
    nums[:] = sorted(list(set(nums)))

    return len(nums)

# Test case1
nums = [1,1,2]
expectedNums = [1,2]

k = removeDuplicates(nums)

assert k == len(expectedNums)

for i in range(k):
    assert nums[i] == expectedNums[i]

# Test case2
nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = [0,1,2,3,4]

k = removeDuplicates(nums)

assert k == len(expectedNums)

for i in range(k):
    assert nums[i] == expectedNums[i]

print("All tests passed")
