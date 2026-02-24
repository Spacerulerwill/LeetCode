from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def traverse(current: int, node: TreeNode) -> bool:
            current += node.val
            if node.left is None and node.right is None:
                return current == targetSum
            if node.left is not None and traverse(node.left):
                return True
            if node.right is not None and traverse(node.right):
                return True
            return False
        if root is None:
            return False
        return traverse(0, root)
