def isOneBitCharacter(bits: list[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == len(bits) - 1


nums = [1,0,0]
print(isOneBitCharacter(nums))

nums = [1,1,1,0]
print(isOneBitCharacter(nums))
