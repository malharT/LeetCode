# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST2(self, root: Optional[TreeNode], min_val, max_val) -> bool:
        valid = True
        if root.left is not None:
            if root.left.val < root.val and root.left.val > min_val:
                valid &= self.isValidBST2(root.left, min_val, root.val)
            else:
                return False
        if not valid:
            return False
        if root.right is not None:
            if root.right.val > root.val and root.right.val < max_val:
                valid &= self.isValidBST2(root.right, root.val, max_val)
            else:
                return False
        return valid


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBST2(root, float('-inf'), float('inf'))
