// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/

// Single Number

/*
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Constraints:

1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.
*/

#include <bits/stdc++.h>
#include <vector>
#include <assert.h>
using namespace std;

// solution
// Time complexity: O(n)
// Space complexity: O(1)
// 
// Runtime: 0 ms, Memory: 20.59 MB
int singleNumber(vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        result ^= num;
    }
    return result;
}

int main() {
    // Test case1
    vector<int> nums = {2,2,1};
    assert(singleNumber(nums) == 1);

    // Test case2
    nums = {4,1,2,1,2};
    assert(singleNumber(nums) == 4);

    nums = {1};
    assert(singleNumber(nums) == 1);

    cout << "All test cases passed." << endl;
}
