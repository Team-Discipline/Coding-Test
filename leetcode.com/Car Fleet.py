"""
https://leetcode.com/problems/car-fleet/
Car Fleet
"""


class Solution:
    def carFleet(self, target: int, position: [int], speed: [int]) -> int:
        """
        Speed will be a coeffecient of equation.
        Position will be a y value of equation.
        From 0 to target, That is range of graph.
        """
        array = list(zip(speed, position))
        array.sort(key=lambda x: x[1], reverse=True)

        # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
        stack = []
        for s, p in array:
            if stack:
                while stack:
                    meet = False
                    ts, tp = stack[-1]
                    if ts < s:
                        hour = 0
                        while hour < target:
                            first = s * hour + p
                            second = ts * hour + tp
                            if first > target or second > target:
                                break
                            elif first == second:
                                meet = True
                                break  # break the while loop.
                            hour += 1
                        else:
                            stack.pop()
                    if not meet:
                        stack.append((s, p))
                    break
            else:
                stack.append((s, p))

        return len(stack)


s = Solution()
assert s.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
assert s.carFleet(10, [0, 4, 2], [2, 1, 3]) == 1
assert s.carFleet(10, [6, 8], [3, 2]) == 2
assert s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
