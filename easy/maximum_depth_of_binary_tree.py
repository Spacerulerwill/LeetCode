# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        def dfs(node: Optional[TreeNode], depth=0):
            nonlocal max_depth
            if not node:
                return
            
            if not node.left and not node.right:
                max_depth = max(max_depth, depth+1)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            
        dfs(root)
        return max_depth

