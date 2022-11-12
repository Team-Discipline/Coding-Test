"""
https://leetcode.com/problems/two-sum/
Two Sum
"""
from itertools import combinations


class Num:
    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index

    def __repr__(self):
        return f'{self.value}({self.index})'


class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        n = []
        for i, v in enumerate(nums):
            n.append(Num(v, i))
        n.sort(key=lambda x: x.value)
        c = combinations(n, 2)

        for i in c:
            if i[0].value + i[1].value == target:
                return [i[0].index, i[1].index]


s = Solution()

print(s.twoSum([-3, 4, 3, 90], 0) == [0, 2])
print(s.twoSum([2, 3, 4], 6) == [0, 2])
print(s.twoSum([3, 3], 6) == [0, 1])
print(s.twoSum([0, 4, 3, 0], 0) == [0, 3])
print(s.twoSum([-3, 4, 3, 90], 0) == [0, 2])
