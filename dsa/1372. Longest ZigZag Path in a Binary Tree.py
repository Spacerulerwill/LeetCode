# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        _max = 0
        def dfs(node: Optional[TreeNode], last_direction: bool, length: int):
            nonlocal _max
            if not node:
                _max = max(_max, length - 1)
                return
            if last_direction:
                dfs(node.left, False, length + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right, True, length + 1)
        if root:
            dfs(root.left, False, 1)
            dfs(root.right, True, 1)
        return _max