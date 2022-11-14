"""
https://www.algoexpert.io/questions/find-closest-value-in-bst
Find Closest Value
"""


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bst(tree: BST, target: int, result: [int]) -> bool:
    # v = tree.value
    # t = target
    if len(result):
        return False
    elif tree is None:
        return True
    elif tree.value == target:
        result.append(tree.value)
        return False
    elif tree.value >= target:
        if bst(tree.left, target, result):
            result.append(tree.value)
        return False
    else:
        if bst(tree.right, target, result):
            result.append(tree.value)
        return False


def findClosestValueInBst(tree: BST, target: int):
    result = []
    bst(tree, target, result)
    print(f'{result[0]=}')
    return result[0]


root = BST(100)
root.left = BST(5)
root.right = BST(502)
root.left.left = BST(2)
root.left.right = BST(15)
root.right.left = BST(204)
root.right.right = BST(55000)
root.left.left.left = BST(1)
root.left.left.right = BST(3)
root.left.right.left = BST(5)
root.left.right.right = BST(22)
root.left.left.left.left = BST(-51)
root.left.left.left.right = BST(1)
root.left.left.left.left.left = BST(-403)
assert findClosestValueInBst(root, -70) == -51
