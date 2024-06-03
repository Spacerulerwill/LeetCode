# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return [[]]
        res = []

        q = deque()
        q.append(root)

        while q:
            len_q = len(q)
            level = []
            for i in range(len_q):
                node = q.popleft()
                if node:
                    level.append(node.value)
                    q.append(node.left)
                    q.append(node.right)
            res.append(level)
        return res