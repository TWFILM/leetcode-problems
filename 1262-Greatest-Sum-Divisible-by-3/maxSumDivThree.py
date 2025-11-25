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

nums = [366,809,6,792,822,181,210,588,344,618,341,410,121,864,191,749,637,169,123,472,358,908,235,914,322,946,738,754,908,272,267,326,587,267,803,281,586,707,94,627,724,469,568,57,103,984,787,552,14,545,866,494,263,157,479,823,835,100,495,773,729,921,348,871,91,386,183,979,716,806,639,290,612,322,289,910,484,300,195,546,499,213,8,623,490,473,603,721,793,418,551,331,598,670,960,483,154,317,834,352]
print(maxSunDivThree(nums))
