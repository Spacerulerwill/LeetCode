# https://leetcode.com/problems/delete-leaves-with-a-given-value/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def is_leaf(node: TreeNode) -> bool:
            return not node.left and not node.right
        
        def dfs(node: Optional[TreeNode]):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            if node.left and node.left.val == target and is_leaf(node.left):
                node.left = None
            if node.right and node.right.val == target and is_leaf(node.right):
                node.right = None
        dfs(root)
        # edge case when root is target
        if root and is_leaf(root) and root.val == target:
            return None
        return root