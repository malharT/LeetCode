# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root_i = len(nums)//2 + len(nums)%2 -1
        root_val = nums[root_i]
        root_node = TreeNode(root_val)
        left_arr = nums[:root_i]
        right_arr = nums[root_i+1:]
        if left_arr:
            root_node.left = self.sortedArrayToBST(left_arr)
        if right_arr:
            root_node.right = self.sortedArrayToBST(right_arr)
        return root_node