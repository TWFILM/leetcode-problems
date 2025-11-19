def findFinalValue(nums: list[int], original: int) -> int:
    while original in nums:
        original *= 2
    return original


nums = [5, 3, 6, 1, 12]
original = 3
print(findFinalValue(nums, original))

nums = [2, 7, 9]
original = 4
print(findFinalValue(nums, original))
