"""
https://www.algoexpert.io/questions/four-number-sum
Four Number Sum
"""


def fourNumberSum(array, targetSum):
    def count(indices):
        ready = sum([array[i] for i in indices])
        if len(indices) >= 4:
            if ready == targetSum:
                results.append([array[i] for i in indices])
            return

        for i in range(indices[-1] + 1, len(array)):
            count(indices + [i])

    results = []
    for i in range(len(array) - 3):
        count([i])
    return results


assert fourNumberSum([5, -5, -2, 2, 3, -3], 0) == [
    [5, -5, -2, 2],
    [5, -5, 3, -3],
    [-2, 2, 3, -3]
]
assert fourNumberSum([1, 2, 3, 4, 5, 6, 7], 10) == [
    [1, 2, 3, 4]
]
assert len(fourNumberSum([1, 2, 3, 4, 5, -5, 6, -6], 5)) == len([
    [2, 3, 5, -5],
    [1, 4, 5, -5],
    [2, 4, 5, -6],
    [1, 3, -5, 6],
    [2, 3, 6, -6],
    [1, 4, 6, -6]  #
])
assert fourNumberSum([7, 6, 4, -1, 1, 2], 16) == [[7, 6, 4, -1], [7, 6, 1, 2]]
