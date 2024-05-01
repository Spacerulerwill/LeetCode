# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        def inorder(root: Optional[TreeNode]) -> bool:
            if not root:
                return True
            valid_left = inorder(root.left)
            if stack and stack[-1] >= root.val:
                return False
            stack.append(root.val)
            valid_right = inorder(root.right)
            return valid_left and valid_right
        return inorder(root)