# https://leetcode.com/problems/deepest-leaves-sum/

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        sum = 0
        q = deque()
        q.append(root)
        while q:
            sum = 0
            len_q = len(q)
            for _ in range(len_q):
                node = q.popleft()
                if not node.left and not node.right:
                    sum += node.val
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
        return sum
