# https://leetcode.com/problems/symmetric-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return True
            if bool(node1) != bool(node2):
                return False
            if node1.val != node2.val:
                return False
            return is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)
        return is_mirror(root, root)