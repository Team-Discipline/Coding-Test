"""
https://leetcode.com/problems/subsets/
Zigzag Conversion
"""


class Solution:
    def dfs(self, nums: [int], given: [int], results):
        if len(given) >= len(nums):
            return

        for num in nums:
            if num in given:
                continue

            new = given.copy()
            new.append(num)
            new.sort()
            if new not in results:
                results.append(new)
                self.dfs(nums, new, results)

    def subsets(self, nums: [int]) -> [[int]]:
        nums.sort()
        results = [[], nums]

        self.dfs(nums, [], results)

        return results


s = Solution()
s.subsets([1, 2, 3])
