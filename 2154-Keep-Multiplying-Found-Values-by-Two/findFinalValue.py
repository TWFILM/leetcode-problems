def findFinalValue(nums: List[int], original: int) -> int:
    while original in nums:
        original *= 2
    return original
