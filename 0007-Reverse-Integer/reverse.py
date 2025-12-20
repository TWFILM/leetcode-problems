# leetcode 7. Reverse Integer
'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Constraints:

-231 <= x <= 231 - 1
'''

# Solution
# Runtime: 40 ms, Memory: 17.53 MB
def reverse(x: int) -> int:
    if x < 0: 
        str_x = str(x)[1:]
        str_x = str_x[::-1]
        int_x = int(str_x)
        if int_x <= 2**31:
            return int_x * -1
    else:
        str_x = str(x)
        str_x = str_x[::-1]
        int_x = int(str_x)
        if int_x <= 2**31 - 1:
            return int_x
    return 0


# Test Cases
x = 123
expected = 321
assert reverse(x) == expected

x = -123
expected = -321
assert reverse(x) == expected

x = 120
expected = 21
assert reverse(x) == expected

print("All test cases passed")

