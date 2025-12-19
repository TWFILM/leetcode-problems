# leetcode 6 Zigzag Conversion
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

# Solution: Simulation
# Time Complexity: O(n)
# Runtime: 7 ms, Memory: 17.42 MB
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s

    new_s = ""
    mid = False
    i = 0
    while i < len(s):
        if mid:
            new_s = new_s + s[i:i+numRows-2] + " "
            i += numRows - 2
            mid = False
        else:
            new_s = new_s + s[i:i+numRows] + " "
            i += numRows
            mid = True

    result = [""] * numRows
    index, step = 0, 1
    for char in new_s:
        if index == -1 or index == numRows:
            step = -step
            result[index+step] += char
            index += step
        else:
            result[index] += char
        index += step

    result = [char.replace(" ", "") for char in result]
    return "".join(result)


# Test Cases
s = "PAYPALISHIRING"
numRows = 3

expected = "PAHNAPLSIIGYIR"
assert convert(s, numRows) == expected

s = "PAYPALISHIRING"
numRows = 4

expected = "PINALSIGYAHRPI"
assert convert(s, numRows) == expected

s = "A"
numRows = 1

expected = "A"
assert convert(s, numRows) == expected

s = "AB"
numRows = 1

expected = "AB"
assert convert(s, numRows) == expected

print("All test cases passed")

