# https://leetcode.com/problems/sum-root-to-leaf-numbers

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], path_sum: int) -> int:
            if not node:
                return 0
            path_sum = (path_sum * 10) + node.val
            if not node.left and not node.right:
                return path_sum
            else:
                return dfs(node.left, path_sum) + dfs(node.right, path_sum)
        return dfs(root, 0)
