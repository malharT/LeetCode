# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '^#'
        s = '^' + str(root.val)
        s += self.serialize(root.left)
        s += self.serialize(root.right)
        return s

    def helper(self, data):
        if data == '':
            return None, ''
        data = data[1:]
        next_tok = data.find('^')
        if next_tok == -1:
            token = data
        else:
            token = data[:next_tok]
        data = data[next_tok:]
        if token != '#':
            node = TreeNode(int(token))
            node.left, data = self.helper(data)
            node.right, data = self.helper(data)
        else:
            node = None
        return node, data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self.helper(data)[0]

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))