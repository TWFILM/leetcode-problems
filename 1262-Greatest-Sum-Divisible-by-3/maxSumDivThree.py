def powerSet(nums: list[int]) -> list[list[int]]:
    if nums == []:
        return [[]]

    head = [nums[0]]
    tail = powerSet(nums[1:])
    result = list(map(lambda x: x + head, tail)) + tail
    return result

def maxSunDivThree(nums: list[int]) -> int:
    result = list(map(sum, powerSet(nums)))
    result = list(filter(lambda x: x % 3 == 0, result))

    if result == []:
        return 0
    return max(result)

nums = [3,6,5,1,8]
print(maxSunDivThree(nums))

nums = [4]
print(maxSunDivThree(nums))

nums = [1,2,3,4,4]
print(maxSunDivThree(nums))
