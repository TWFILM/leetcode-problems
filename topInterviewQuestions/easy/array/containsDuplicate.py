# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

### Contains Duplicate

'''
Given an integer array "nums", return "true" if any value appears at least twice in the array, and return "false" if every element is distinct.

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
'''

# Solution
# Runtime: 20 ms, Memory: 31.56 MB
def containsDuplicate(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

# Test case
nums = [1,2,3,1]
expected = True

k = containsDuplicate(nums)
'''
Explanation:
The element 1 occurs at the indices 0 and 3.
'''
assert k == expected

nums = [1,2,3,4]
expected = False

k = containsDuplicate(nums)
'''
Explanation:
All elements are distinct.
'''
assert k == expected

nums = [1,1,1,3,3,4,3,2,4,2]
expected = True

k = containsDuplicate(nums)
assert k == expected

print("All tests passed")
