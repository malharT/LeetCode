# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, nums, k):
        if len(nums) == k or root is None:
            return
        self.traverse(root.left, nums, k)
        if len(nums) != k:
            nums.append(root.val)
        self.traverse(root.right, nums, k)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        self.traverse(root, nums, k)
        return nums[-1]