"""
https://www.algoexpert.io/questions/min-number-of-coins-for-change
Min Number Of Coins For Change
"""


def minNumberOfCoinsForChange(n, denoms):
    if n == 0: return 0
    denoms = list(filter(lambda x: x <= n, denoms))  # Cut off numbers when bigger than n.
    denoms.sort(reverse=True)
    num = 1
    while True:
        target = n
        if denoms[0] * num < target:
            num += 1
            continue
        elif denoms[-1] * num > target:
            # No hope.
            break

        results = []

        def recur(array):
            if len(array) != num:
                for number in denoms:
                    results.append(recur(array + [number]))
            return sum(array) == target

        recur([])
        if any(results):
            return num
        else:
            num += 1
    return -1


assert minNumberOfCoinsForChange(7, [3, 7]) == 1
assert minNumberOfCoinsForChange(135, [39, 45, 130, 40, 4, 1, 60, 75]) == 2
assert minNumberOfCoinsForChange(7, [1, 5, 10]) == 3
