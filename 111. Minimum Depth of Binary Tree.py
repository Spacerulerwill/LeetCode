# https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], depth:int=0):
            nonlocal _min
            if not node.left and not node.right:
                _min = min(_min, depth+1)
            if depth < _min - 1:
                if node.left:
                    dfs(node.left, depth + 1)
                if node.right:
                    dfs(node.right, depth + 1)
        if not root:
            return 0
        _min = float("inf")
        dfs(root)
        return _min
