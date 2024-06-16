# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        res = []

        q = deque()
        q.append(root)

        while q:
            len_q = len(q)
            level = []
            for _ in range(len_q):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        res.reverse()
        return res