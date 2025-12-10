# Leetcode 3. Longest Substring Without Repeating Characters
# Give a string s, find the length of the longest substring without repeating characters.
'''
Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
'''

# Dynamic Programming
'''
1. Create a dp array of size len(s).
2. Initialize dp[0] to 1.
3. Iterate through the string s with index i.
4. If s[i] is in last_seen, update dp[i] to min(dp[i - 1] + 1, i - last_seen[s[i]]).
5. Update last_seen[s[i]] to i.
6. Update max_len to max(max_len, dp[i]).
'''
# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 23 ms, Memory: 17.86 MB
def lengthOfLongestSubstring(s: str) -> int:
    if not s: return 0

    dp = [0] * len(s)
    dp[0] = 1

    last_seen = {s[0]: 0}
    max_len = 1

    for i in range(1, len(s)):
        if s[i] in last_seen:
            dist = i - last_seen[s[i]]
        else:
            dist = i + 1

        dp[i] = min(dp[i - 1] + 1, dist)

        last_seen[s[i]] = i
        max_len = max(max_len, dp[i])

        return max_len

# Sliding Window
'''
1. Use a dictionary to store the last seen index of each character.
2. Iterate through the string s with index i.
3. If s[i] is in char_map, update start to max(start, char_map[s[i]] + 1).
4. Update char_map[s[i]] to i.
5. Update max_len to max(max_len, i - start + 1).
'''
# Time Complexity: O(n)
# Space Complexity: O(n)
# Runtime: 19 ms, Memory: 17.66 MB
def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    start = 0
    max_len = 0

    for i in range(len(s)):
        if s[i] in char_map:
            start = max(start, char_map[s[i]] + 1)

        char_map[s[i]] = i

        current_len = i - start + 1
        max_len = max(max_len, current_len)

    return max_len

# Test Cases
s = 'abcabcbb'
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Note that "bca" is also a valid answer, with the same length.
print(lengthOfLongestSubstring(s))

s = 'bbbbb'
# Output: 1
# Explanation: The answer is "b", with the length of 1.
print(lengthOfLongestSubstring(s))

s = 'pwwkew'
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
print(lengthOfLongestSubstring(s))

s = " "
# Output: 1
# Explanation: The answer is " ", with the length of 1.
print(lengthOfLongestSubstring(s))

s = "abba"
# Output: 2
# Explanation: The answer is "ab", with the length of 2.
print(lengthOfLongestSubstring(s))

