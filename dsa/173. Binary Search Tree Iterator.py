# https://leetcode.com/problems/binary-search-tree-iterator/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.current = root

    def next(self) -> int:
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left
        self.current = self.stack.pop()
        val = self.current.val
        self.current = self.current.right
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.current is not None

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()