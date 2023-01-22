# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_max_d_and_p(self, root):
        if root is None:
            return 0,0
        max_p_l, max_d_l = self.get_max_d_and_p(root.left)
        max_p_r, max_d_r = self.get_max_d_and_p(root.right)
        return max(max_d_l+max_d_r + 1, max_p_l, max_p_r), 1+max(max_d_l,max_d_r)

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.get_max_d_and_p(root)[0]-1
        