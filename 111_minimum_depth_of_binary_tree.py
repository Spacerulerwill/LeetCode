from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            has_left = node.left is not None
            has_right = node.right is not None
            if not has_left and not has_right:
                return depth
            if has_left:
                queue.append((node.left, depth + 1))
            if has_right:
                queue.append((node.right, depth + 1))
