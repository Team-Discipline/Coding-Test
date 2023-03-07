"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
Maximum Depth of Binary Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = []

        def count(node, depth):
            if node is None:
                result.append(depth - 1)
                return
            count(node.left, depth + 1)
            count(node.right, depth + 1)

        count(root, 1)

        return max(result)
