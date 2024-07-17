# https://leetcode.com/problems/delete-nodes-and-return-forest/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        result = set([root])
        to_delete = set(to_delete)
        def dfs(node: Optional[TreeNode]):
            if not node:
                return None
            res = node
            if node.val in to_delete:
                res = None 
                result.discard(node)
                if node.left:
                    result.add(node.left)
                if node.right:
                    result.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return res
        dfs(root)
        return list(result)
