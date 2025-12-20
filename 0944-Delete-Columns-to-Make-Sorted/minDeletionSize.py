# leetcode 944. Delete Columns to Make Sorted
'''
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

    - For example, strs = ["abc", "bce", "cae"] can be arranged as follows:

    abc
    bce
    cae

You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

Constraints:

n == strs.length
1 <= n <= 100
1 <= strs[i].length <= 1000
strs[i] consists of lowercase English letters.
'''

# Solution
def minDeletionSize(strs: list[str]) -> int:
    n = len(strs)
    cols = len(strs[0])
    col_del = 0

    for col in range(cols):
        for i in range(1, n):
            if strs[i-1][col] > strs[i][col]:
                col_del += 1
                break
 
    return col_del


# Test case
strs = ["cba","daf","ghi"]
'''
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.
'''
expected = 1
assert minDeletionSize(strs) == expected

strs = ["a","b"]
'''
Explanation: The grid looks as follows:
  a
  b
Columns 0 and 1 are sorted, so you do not need to delete any columns.
'''
expected = 0
assert minDeletionSize(strs) == expected

strs = ["zyx","wvu","tsr"]
'''
Explanation: The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
'''
expected = 3
assert minDeletionSize(strs) == expected

