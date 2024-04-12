# https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If root is null, return
        if not root:
            return root
        
        # swap the roots
        root.left, root.right = root.right, root.left

        # do the same for our child roots
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root