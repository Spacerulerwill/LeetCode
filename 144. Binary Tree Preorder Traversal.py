# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        def inner(node: Optional[TreeNode]):
            if not node:
                return
            result.append(node.val)
            inner(node.left)
            inner(node.right)
        inner(root)
        return result