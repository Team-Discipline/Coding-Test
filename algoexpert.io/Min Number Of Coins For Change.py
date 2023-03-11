"""
https://www.algoexpert.io/questions/min-number-of-coins-for-change
Min Number Of Coins For Change
"""


def minNumberOfCoinsForChange(n, denoms):
    dp = [float('inf') for _ in range(n + 1)]
    dp[0] = 0
    for denom in denoms:
        for amount in range(len(dp)):
            if denom <= amount:
                dp[amount] = min(dp[amount], dp[amount - denom] + 1)
    return dp[n] if dp[n] != float('inf') else -1


assert minNumberOfCoinsForChange(7, [3, 7]) == 1
assert minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1, 60, 75]) == 2
assert minNumberOfCoinsForChange(7, [1, 5, 10]) == 3
