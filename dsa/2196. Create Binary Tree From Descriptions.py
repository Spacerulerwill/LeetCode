# https://leetcode.com/problems/create-binary-tree-from-descriptions/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        if len(descriptions) == 0:
            return None
        # determine root node
        set_of_children = set(description[1] for description in descriptions)
        for description in descriptions:
            if description[0] not in set_of_children:
                root_val = description[0]
        nodes = {}
        for description in descriptions:
            parent = description[0]
            child = description[1]
            isLeft = True if description[2] == 1 else False
            if parent in nodes:
                if isLeft:
                    nodes[parent][0] = child
                else:
                    nodes[parent][1] = child
            else:
                if isLeft:
                    nodes[parent] = [child, None]
                else:
                    nodes[parent] = [None, child]
        # recursively build the tree
        def build(val:Optional[int]) -> Optional[TreeNode]:
            if val is None:
                return None
            children = nodes.get(val, None)
            if children is None:
                return TreeNode(val)
            return TreeNode(val, build(children[0]), build(children[1]))
        return build(root_val)