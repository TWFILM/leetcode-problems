def prefixesDivBy5(nums: list[int]) -> list[bool]:
    answer = []
    x = 0
    for bit in nums:
        x = x*2 + bit
        answer.append(x % 5 == 0)

    return answer

nums = [0,1,1]
print(prefixesDivBy5(nums))

nums = [1,1,1]
print(prefixesDivBy5(nums))
