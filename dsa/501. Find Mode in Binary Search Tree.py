# https://leetcode.com/problems/find-mode-in-binary-search-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        
        current_val = None
        current_count = 0
        max_count = 0
        modes = []
        
        def handle(value:int):
            nonlocal current_val, current_count, max_count, modes
            if value != current_val:
                current_val = value
                current_count = 1
            else:
                current_count += 1

            if current_count > max_count:
                max_count = current_count
                modes = [value]
            elif current_count == max_count:
                modes.append(value)

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            dfs(node.left)
            handle(node.val)
            dfs(node.right)
        dfs(root)
        return modes