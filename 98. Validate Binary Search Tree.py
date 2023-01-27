# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, min_val, max_val):
        if root is None:
            return True
        if root.val > min_val and root.val < max_val:
            return self.traverse(root.left, min_val, root.val) and self.traverse(root.right, root.val, max_val)
        else:
            return False


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, float('-inf'), float('inf'))