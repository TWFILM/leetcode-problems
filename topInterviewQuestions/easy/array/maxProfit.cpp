// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

// Best Time to Buy and Sell Stock

/*
You are given an array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the maximum profit you can achieve.

Constraints:

1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
*/

#include <bits/stdc++.h>
#include <vector>
#include <assert.h>
using namespace std;

// solution
// Time complexity: O(n)
// Space complexity: O(1)
//
// Runtime: 0 ms, Memory: 17.01 MB
int maxProfit(vector<int>& prices) {
    int maxProfit = 0;
    for (int i = 1; i < prices.size(); i++) {
        if (prices[i] > prices[i - 1]) {
            maxProfit += prices[i] - prices[i - 1];
        }
    }
    return maxProfit;
}

int main() {
    // Test case1
    vector<int> prices = {7,1,5,3,6,4};
    assert(maxProfit(prices) == 7);

    // Test case2
    prices = {1,2,3,4,5};
    assert(maxProfit(prices) == 4);

    // Test case3
    prices = {7,6,4,3,1};
    assert(maxProfit(prices) == 0);

    cout << "All test cases passed." << endl;
}
