# leetcode 5 Longest Palindromic Substring
'''
Given a string s, return the longest palindromic substring in s.

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''

# My Solution: Dynamic Programming
# Time complexity: O(n^2)
# Space complexity: O(n^2)
# Runtime: 1856 ms, Memory: 25.54 MB 
def longestPalindrome(s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    start = 0
    maxLen = 1

    # all substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True

    # check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            if maxLen == 1:
                start = i
                maxLen = 2

    # check for substrings of length > 2
    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if l > maxLen:
                    start = i
                    maxLen = l

    return s[start:start + maxLen]


# Test case
s = "babad"
expected = "bab"
# Explanation: "aba" is also a valid answer.
assert longestPalindrome(s) == expected

s = "cbbd"
expected = "bb"
assert longestPalindrome(s) == expected

print("All test cases passed")

