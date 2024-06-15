# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        def dfs(node):
            if not node:
                nodes.append("N")
                return
            nodes.append(str(node.val))  # Append the value of the node, not the node itself
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(nodes)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tree_list = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            next = tree_list[i]
            if next == "N":
                i += 1
                return None
            new = TreeNode(int(next))
            i += 1
            new.left = dfs()
            new.right = dfs()
            return new
        return dfs()
    
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))