"""
https://leetcode.com/problems/house-robber/
House Robber
"""


class Solution:
    def rob(self, nums: [int]) -> int:
        results = [0 for _ in nums]

        for i in range(len(nums)):
            if i < 2:
                results[i] = nums[i]
            else:
                results[i] = max(results[:i - 1]) + nums[i]

        return max(results)


s = Solution()
assert s.rob([1, 2, 3, 1]) == 4
