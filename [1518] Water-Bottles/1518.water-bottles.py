#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totol_drunk = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            new_bottles = empty_bottles // numExchange
            totol_drunk += new_bottles
            empty_bottles = empty_bottles % numExchange + new_bottles
        
        return totol_drunk
# @lc code=end

