"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Best Time to Buy and Sell Stock
"""


class Solution:

    def maxProfit(self, prices: [int]) -> int:
        result = 0

        # Judge if it is descending.
        is_descending = True
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                is_descending = False

        if is_descending:
            return 0
        else:
            while prices:
                m = min(prices)
                minimum_index = prices.index(m)
                rearrange = prices[minimum_index + 1:]

                for price in rearrange:
                    if price - m > result:
                        result = price - m

                prices.pop(minimum_index)

            return result


s = Solution()
assert s.maxProfit([2, 4, 1]) == 2
assert s.maxProfit([7, 6, 4, 3, 1]) == 0
assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
