"""
https://leetcode.com/problems/longest-increasing-subsequence/
Longest Increasing Subsequence
"""
from typing import List

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


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        maxval = 1

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxval = max(maxval, dp[i])

        return maxval


s = Solution()
assert s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
