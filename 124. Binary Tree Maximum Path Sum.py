# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root):
        if root is None:
            return float('-inf'), 0
        l_max_p, l_path_sum = self.traverse(root.left)
        r_max_p, r_path_sum = self.traverse(root.right)
        combined_p = l_path_sum+root.val+r_path_sum
        cont_l_path = root.val+l_path_sum
        cont_r_path = root.val+r_path_sum
        return (max(combined_p, l_max_p,
                    r_max_p, cont_l_path,
                    cont_r_path, root.val),
                max(cont_l_path, cont_r_path, root.val))


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_p, p = self.traverse(root)
        return max(max_p, p)