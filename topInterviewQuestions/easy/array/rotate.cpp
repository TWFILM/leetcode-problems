// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/

// Rotate Array

/*
Given an array, rotate the array to the right by k steps, where k is non-negative.

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
*/

#include <bits/stdc++.h>
#include <vector>
#include <assert.h>
using namespace std;

// solution
// Time complexity: O(n)
// Space complexity: O(1)
//
// Runtime: 0 ms, Memory: 29.39 MB
void rotate(vector<int>& nums, int k) {
    k = k % nums.size();
    reverse(nums.begin(), nums.end());
    reverse(nums.begin(), nums.begin() + k);
    reverse(nums.begin() + k, nums.end());
}

int main() {
    // Test case1
    vector<int> nums = {1,2,3,4,5,6,7};
    int k = 3;
    vector<int> expectedNums = {5,6,7,1,2,3,4};

    rotate(nums, k);

    assert(nums == expectedNums);

    // Test case2
    nums = {-1,-100,3,99};
    k = 2;
    expectedNums = {3,99,-1,-100};

    rotate(nums, k);

    assert(nums == expectedNums);

    cout << "All test cases passed." << endl;
}
