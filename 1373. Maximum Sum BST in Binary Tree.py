# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumValidBST(self, root):
        left_exists = False
        right_exists = False
        if root.left is not None:
            left_exists = True
            max_sum_l, cont_sum_l, min_l, max_l = self.maxSumValidBST(
                root.left)
        if root.right is not None:
            right_exists = True
            max_sum_r, cont_sum_r, min_r, max_r = self.maxSumValidBST(
                root.right)
        if left_exists and right_exists:
            if (root.left.val < root.val and root.right.val > root.val
                and cont_sum_r is not None and cont_sum_l is not None
                and root.val > max_l and root.val < min_r):
                new_sum = cont_sum_r + cont_sum_l + root.val
                max_sum = max(new_sum, max_sum_l, max_sum_r)
            else:
                new_sum = None
                max_sum = max(max_sum_l, max_sum_r)
            return max_sum, new_sum, min(root.val, min_l, min_r, max_l, max_r), max(root.val, min_l, min_r, max_l, max_r)
        elif left_exists:
            if root.left.val < root.val and cont_sum_l is not None and root.val > max_l:
                new_sum = cont_sum_l + root.val
                max_sum = max(new_sum, max_sum_l)
            else:
                new_sum = None
                max_sum = max_sum_l
            return max_sum, new_sum, min(root.val, min_l, max_l), max(root.val, min_l, max_l)
        elif right_exists:
            if root.right.val > root.val and cont_sum_r is not None and root.val < min_r:
                new_sum = cont_sum_r + root.val
                max_sum = max(new_sum, max_sum_r)
            else:
                new_sum = None
                max_sum = max_sum_r
            return max_sum, new_sum, min(root.val, min_r, max_r), max(root.val, min_r, max_r)
        else:
            return root.val, root.val, root.val, root.val

        
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum, cont_sum, min_val, max_val = self.maxSumValidBST(root)
        if max_val < 0:
            return 0
        else:
            return max_sum