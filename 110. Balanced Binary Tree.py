# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_height(self, root):
        if root is None:
            return True, 0
        ans_l, l_h = self.get_height(root.left)
        ans_r, r_h = self.get_height(root.right)
        ans = ans_l and ans_r and (abs(l_h-r_h) <= 1)

        return ans, 1 + max(l_h, r_h)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.get_height(root)[0]
