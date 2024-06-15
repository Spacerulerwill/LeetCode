# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        q = deque()
        q.append(root)
        max_level = 1
        max_level_sum = float("-inf")
        level = 1
        while q:
            len_q = len(q)
            level_sum = 0
            for _ in range(len_q):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)     
            if level_sum > max_level_sum:
                max_level = level
                max_level_sum = level_sum
            level += 1
        return max_level