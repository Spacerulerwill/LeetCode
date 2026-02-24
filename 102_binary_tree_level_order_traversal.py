from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            has_left = node.left is not None
            has_right = node.right is not None
            # process
            if len(result) < depth:
                result.append([])
            result[depth - 1].append(node.val)
            if has_left:
                queue.append((node.left, depth + 1))
            if has_right:
                queue.append((node.right, depth + 1))
        return result