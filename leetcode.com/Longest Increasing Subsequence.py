"""
https://leetcode.com/problems/longest-increasing-subsequence/
Longest Increasing Subsequence
"""

"""
\ X 0 1 0 3 2 3
X 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 0 2 2 2 2 2 2
0 0 2 2 2 2 2 2
3 0 3 3 3 3 3 3
2 0 3 3 3 3 3 3
3 0 4 4 4 4 4 4
"""

s = Solution()
assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
