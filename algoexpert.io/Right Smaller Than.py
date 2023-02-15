"""
https://www.algoexpert.io/questions/right-smaller-than
Right Smaller Than
"""


class BST:
    def __init__(self, index, value):  # , size_of_left_subtree=None):
        self.index = index
        self.value = value
        # self.size_of_left_subtree = size_of_left_subtree
        self.left = None
        self.right = None

    def __str__(self):
        return f'[{self.value} ({self.index}th) / {self.left} {self.right}]'

    def __repr__(self):
        return f'[{self.value} ({self.index}th) / {self.left} {self.right}]'


def c(array):
    if not array:
        return None

    r = array.pop(0)
    root = BST(r[0], r[1])
    left, right = [], []
    for i, num in array:
        if root.value > num:
            left.append((i, num))
        else:
            right.append((i, num))

    root.left = c(left)
    root.right = c(right)
    # if root.left is not None:
    #     root.size_of_left_subtree = root.left.size_of_left_subtree + 1
    # else:
    #     root.size_of_left_subtree = 0

    return root


def get_count(tree):
    if not tree:
        return -1

    left = get_count(tree.left) + 1
    right = get_count(tree.right) + 1

    return left + right


def rightSmallerThan(array):
    array = [(i, array[i]) for i in range(len(array))]
    r = c(array)
    print(f'{r=}')


assert rightSmallerThan([8, 5, 11, -1, 3, 4, 2]) == [5, 4, 4, 0, 1, 1, 0]
