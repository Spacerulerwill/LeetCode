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
        def dfs(node: Optional[TreeNode], last_left:bool, depth:int):
            nonlocal _max
            if not node:
                _max = max(_max, depth)
                return
            if last_left:
                dfs(node.right, not last_left, depth+1)
            else:
                dfs(node.left, not last_left, depth+1)
        dfs(root, False, 0)
        dfs(root, True, 0)
        return _max