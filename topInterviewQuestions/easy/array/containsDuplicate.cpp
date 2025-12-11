// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

// Contains Duplicate

/*
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
*/

#include <bits/stdc++.h>
#include <vector>
#include <assert.h>
using namespace std;

// solution
// Time complexity: O(nlogn)
// Space complexity: O(1)
bool containsDuplicate(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0; i < nums.size() - 1; i++) {
        if (nums[i] == nums[i + 1]) {
            return true;
        }
    }
    return false;
}

int main() {
    // Test case1
    vector<int> nums = {1,2,3,1};
    assert(containsDuplicate(nums) == true);

    // Test case2
    nums = {1,2,3,4};
    assert(containsDuplicate(nums) == false);

    // Test case3
    nums = {1,1,1,3,3,4,3,2,4,2};
    assert(containsDuplicate(nums) == true);

    cout << "All test cases passed." << endl;
}
