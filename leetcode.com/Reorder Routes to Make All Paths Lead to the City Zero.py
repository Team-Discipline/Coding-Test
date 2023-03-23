"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
Reorder Routes to Make All Paths Lead to the City Zero
"""
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections.sort()
        count = 0

        table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for dep, arr in connections:
            table[arr][dep] = table[dep][arr] = 1  # mark up as undirected graph

        def validate(target: int, visited: List[int]):
            nonlocal table, count, n
            for i, val in enumerate(table[target]):
                if val == 1 and i not in visited:
                    if [target, i] in connections:  # If direction is reversed.
                        count += 1
                    validate(i, visited + [i])

        validate(0, [0])

        return count


s = Solution()
assert s.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
