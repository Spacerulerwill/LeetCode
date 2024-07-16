# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(node:Optional[TreeNode], path:list[str], target:int):
            if node is None:
                return False
            if node.val == target:
                return True
            path.append('L')
            if find_path(node.left, path, target):
                return True
            path.pop()
            path.append('R')
            if find_path(node.right, path, target):
                return True
            path.pop()
            return False

        path_to_start = []
        path_to_dest = []
        find_path(root, path_to_start, startValue)
        find_path(root, path_to_dest, destValue)

        # find paths from root 
        shortest_length = min(len(path_to_start), len(path_to_dest))
        # remove longest common prefix
        i = 0
        while i < shortest_length and path_to_start[i] == path_to_dest[i]:
            i += 1
        path_to_start = path_to_start[i:]
        path_to_dest = path_to_dest[i:]
        return "U" * len(path_to_start) + "".join(path_to_dest)
