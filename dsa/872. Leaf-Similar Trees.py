# https://leetcode.com/problems/leaf-similar-trees/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], output:list[int]):
            if not node:
                return
            if not node.left and not node.right:
                output.append(node.val)
            dfs(node.left, output)
            dfs(node.right, output)
        output1 = []
        dfs(root1, output1)
        output2 = []
        dfs(root2, output2)
        return output1 == output2