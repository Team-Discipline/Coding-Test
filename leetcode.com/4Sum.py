"""
https://leetcode.com/problems/4sum/description/
4Sum
"""


class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        nums.sort()
        results = []

        left, right = 0, len(nums) - 1
        while left < right:
            ready = [nums[left], nums[right]]
            rest = target - sum(ready)
            start, end = left + 1, right - 1
            while start < end:
                r = [nums[start], nums[end]]
                if sum(r) == rest:
                    if ready + r not in results:
                        results.append(ready + r)
                    start += 1
                elif sum(r) > rest:
                    end -= 1
                elif sum(r) < rest:
                    start += 1
            left += 1

        left, right = 0, len(nums) - 1
        while left < right:
            ready = [nums[left], nums[right]]
            rest = target - sum(ready)
            start, end = left + 1, right - 1
            while start < end:
                r = [nums[start], nums[end]]
                if sum(r) == rest:
                    if ready + r not in results:
                        results.append(ready + r)
                    end -= 1
                elif sum(r) > rest:
                    end -= 1
                elif sum(r) < rest:
                    start += 1
            right -= 1

        return list(map(lambda x: sorted(x), results))


s = Solution()
assert s.fourSum([-3, -1, 0, 2, 4, 5], 2) == [[-3, -1, 2, 4]]
assert s.fourSum([-2, -1, -1, 1, 1, 2, 2], 0)
assert s.fourSum([-3, -1, 0, 2, 4, 5], 0) == [[-3, -1, 0, 4]]
