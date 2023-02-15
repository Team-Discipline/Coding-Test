"""
https://www.algoexpert.io/questions/min-rewards
Min Rewards
"""


def minRewards(scores):
    rewards = [1] * len(scores)
    for i in range(1, len(scores)):
        if scores[i - 1] > scores[i]:
            rewards[i] = 1
            # Check back through
            for index in range(i, 0, -1):
                if rewards[index] == rewards[index - 1] and scores[index - 1] > scores[index]:
                    rewards[index - 1] = rewards[index] + 1
        else:
            rewards[i] = rewards[i - 1] + 1

    return sum(rewards)


assert minRewards([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]) == 15
assert minRewards([5, 10]) == 3
assert minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]) == 25
assert minRewards([0, 4, 2, 1, 3]) == 9
