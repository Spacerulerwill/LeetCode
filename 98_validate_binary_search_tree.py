from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last = None

        def traverse(node: Optional[TreeNode]) -> bool:
            nonlocal last
            # no node
            if node is None:
                return True
            if not traverse(node.left):
                return False
            if last is not None and node.val <= last:
                return False
            last = node.val
            return traverse(node.right)

        return traverse(root)
