from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth_limit: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode], current_depth:int=1):
            if not node:
                return
            if current_depth + 1 == depth_limit:
                prev_left = node.left
                prev_right = node.right
                node.left = TreeNode(val, prev_left, None)
                node.right = TreeNode(val, None, prev_right)
            else:
                dfs(node.left, current_depth + 1)
                dfs(node.right, current_depth + 1)
        
        # handle depth limit of 1 differently
        if depth_limit == 1:
            new_node = TreeNode(val, root, None)
            return new_node
        else:
            dfs(root)
            return root

if __name__ == "__main__":
    # test case tree
    #      2
    #    2   2
    #   2 2 2 2
    solution = Solution()
    root = TreeNode(2, TreeNode(2, TreeNode(2), TreeNode(2)), TreeNode(2, TreeNode(2), TreeNode(2)))
    solution.addOneRow(root, 1, 4)
    