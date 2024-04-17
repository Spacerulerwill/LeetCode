from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        _min = ""
        def dfs(node: Optional[TreeNode], current_string: str):
            nonlocal _min
            if not node:
                return
            current_string += chr(97 + node.val)
            if not node.left and not node.right:
                if _min == "":
                    _min = current_string[::-1]
                else:
                    _min = min(_min, current_string[::-1])
            else:
                dfs(node.left, current_string)
                dfs(node.right, current_string)
        dfs(root, "")
        return _min