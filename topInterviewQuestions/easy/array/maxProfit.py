# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

### Best Time to Buy and Sell Stock

'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

Constraints:

1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
'''

# Solution
def maxProfit(prices: list[int]) -> int:
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit

# Test case1
prices = [7,1,5,3,6,4]
expected = 7

k = maxProfit(prices)

assert k == expected

# Test case2
prices = [1,2,3,4,5]
expected = 4

k = maxProfit(prices)

assert k == expected

# Test case3
prices = [7,6,4,3,1]
expected = 0

k = maxProfit(prices)

assert k == expected

print("All tests passed")
