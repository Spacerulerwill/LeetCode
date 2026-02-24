from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def innerSymmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True
            elif left is None:
                return False
            elif right is None:
                return False
            elif left.val != right.val:
                return False
            else:
                return innerSymmetric(left.left, right.right) and innerSymmetric(left.right, right.left)
        return innerSymmetric(root.left, root.right)
        