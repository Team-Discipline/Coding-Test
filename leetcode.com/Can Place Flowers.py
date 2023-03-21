"""
https://leetcode.com/problems/can-place-flowers/
Can Place Flowers
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        # Another solution with O(1) space complexity
        for i in range(len(flowerbed)):
            if n == 0:
                return True
            if ((i == 0 or flowerbed[i - 1] == 0)  # If at the first element or the previous element equals to 0
                    and (flowerbed[i] == 0)  # If current element equals to 0
                    and (i == len(flowerbed) - 1 or flowerbed[
                        i + 1] == 0)):  # If at the last element or the next element equals to 0
                # Place flower at the current position
                flowerbed[i] = 1
                n -= 1

        return n == 0


s = Solution()
assert s.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) == False
assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
