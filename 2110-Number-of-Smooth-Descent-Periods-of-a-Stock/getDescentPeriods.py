# leetcode 2110 Number of Smooth Descent Periods of a Stock
'''
You are given a 0-indexed integer array prices, where prices[i] is the price of a given stock on the ith day.

Find the number of smooth descent periods of a stock.

A smooth descent period is a sequence of consecutive days such that each day's price is strictly lower than the following day's price.

Return the number of smooth descent periods of a stock.

Constraints:

1 <= prices.length <= 10^5
1 <= prices[i] <= 10^5
'''

# Solution
# Runtime: 80 ms, Memory: 29.95 MB
def getDescentPeriods(prices: list[int]) -> int:
    output = 0
    start = 0
    i = 1
    while i < len(prices):
        if prices[i - 1] - 1 != prices[i]:
            n = i - start
            output += int((n * (n + 1)) / 2)

            start = i
        i += 1

    n = i - start
    output += int((n * (n + 1)) / 2)
    return output

# Test Case
prices = [3, 2, 1, 4]

output = 7
'''
Explanation: There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.
'''
assert getDescentPeriods(prices) == output

prices = [8, 6, 7, 7]

output = 4
'''
Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.
'''
assert getDescentPeriods(prices) == output

prices = [1]

output = 1
assert getDescentPeriods(prices) == output

print("All test cases passed")
