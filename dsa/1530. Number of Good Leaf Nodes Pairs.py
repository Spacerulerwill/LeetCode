# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/?envType=daily-question&envId=2024-07-18

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        result = 0
        def dfs(node: Optional[TreeNode]) -> list[int]:
            nonlocal result
            if not node:
                return []
            # if its  aleaf ditsnace is one
            if not node.left and not node.right:
                return [1]
            # we must do the left distances and right distances seperately
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            # check all combinations
            for left_dist in left_distances:
                for right_dist in right_distances:
                    if left_dist + right_dist <= distance:
                        result += 1
            return [d+1 for d in left_distances + right_distances]
        dfs(root)
        return result