"""
https://leetcode.com/problems/jump-game-ii/description/
Jump Game II
"""

# class Solution:
#     """
#     Very basic, slow solution. (even can't pass all tests)
#     """
#
#     def jump(self, nums: List[int]) -> int:
#         res = [math.inf]
#
#         def count(i: int, c: int):
#             nonlocal res
#             if i >= len(nums) - 1:
#                 res.append(c)
#                 return
#
#             for amount in range(nums[i], 0, -1):
#                 if c > min(res):
#                     break
#                 count(i + amount, c + 1)
#
#         count(0, 0)
#
#         return min(res)
