# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.right is None and root.left is None:
            return root
        else:
            if root.left is not None:
                self.invertTree(root.left)
            if root.right is not None:
                self.invertTree(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
            return root
