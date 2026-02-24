from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        _max = 0
        def inner(current_depth: int, node: Optional[TreeNode]):
            nonlocal _max
            # empty node
            if not node:
                return
            # leaf node
            if not node.left and not node.right:
                _max = max(_max, current_depth + 1)
            inner(current_depth + 1, node.left)
            inner(current_depth + 1, node.right)
        inner(0, root)
        return _max 

