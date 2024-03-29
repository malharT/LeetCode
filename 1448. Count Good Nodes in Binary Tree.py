# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, max_val, count):
        if root is None:
            return count
        if root.val >= max_val:
            count += 1
        max_val = max(root.val, max_val)
        count = self.traverse(root.left, max_val, count)
        count = self.traverse(root.right, max_val, count)
        return count

    def goodNodes(self, root: TreeNode) -> int:
        return self.traverse(root, root.val, 0)