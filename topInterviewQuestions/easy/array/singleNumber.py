# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

### Single Number

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:

1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.
'''

# Solution
# Runtime: 5784 ms, Memory: 19.57 MB
def singleNumber(nums: list[int]) -> int:
    sortedNums = sorted(nums, key=nums.count)
    return sortedNums[0]

# Better Solution
# Runtime 0 ms, Memory: 19.58 MB
def singleNumber(nums: list[int]) -> int:
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans

# Test case
nums = [2,2,1]
expected = 1

k = singleNumber(nums)

assert k == expected

nums = [4,1,2,1,2]
expected = 4

k = singleNumber(nums)

assert k == expected

nums = [1]
expected = 1

k = singleNumber(nums)

assert k == expected

print("All tests passed")
