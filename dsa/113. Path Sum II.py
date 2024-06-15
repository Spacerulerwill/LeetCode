# https://leetcode.com/problems/path-sum-ii/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> list[list[int]]:
        result = []
        def dfs(node:Optional[TreeNode], current:list[int], sum:int):
            if not node:
                return
            current.append(node.val)
            sum += node.val
            if not node.left and not node.right and sum == targetSum:
                result.append(current[:])
            else:
                dfs(node.left, current, sum)
                dfs(node.right, current, sum)
            current.pop()
            sum -= node.val
        dfs(root, [], 0)
        return result
        