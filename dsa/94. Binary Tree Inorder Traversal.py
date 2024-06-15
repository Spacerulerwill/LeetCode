# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        def inner(node: Optional[TreeNode]):
            if not node:
                return
            inner(node.left)
            result.append(node.val)
            inner(node.right)
        inner(root)
        return result
