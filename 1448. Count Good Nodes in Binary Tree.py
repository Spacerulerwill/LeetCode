# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node: Optional[TreeNode], _max:int):
            nonlocal count
            if not node:
                return
            _max = max(_max, node.val)
            if (node.val >= _max):
                count += 1
            dfs(node.left, _max)
            dfs(node.right, _max)
        dfs(root, float("-inf"))
        return count