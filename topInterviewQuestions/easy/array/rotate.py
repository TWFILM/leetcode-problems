# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

### Rotate Array

'''
Given an integer array "nums", rotate the array to the right by "k" steps, where "k" is non-negative.

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
'''

# Solution
# Runtime: 0 ms, Memory: 25.25 MB
def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

# Test case
nums = [1,2,3,4,5,6,7]
k = 3

rotate(nums, k)
'''
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
# Output
assert nums == [5,6,7,1,2,3,4]

nums = [-1,-100,3,99]
k = 2

rotate(nums, k)
'''
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''
# Output
assert nums == [3,99,-1,-100]

print("All tests passed")
