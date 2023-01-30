# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def set_right(self, level, val, right):
        if level == len(right):
            right.append(val)
        else:
            right[level] = val

    def traverse(self, root, level, right):
        if root is not None:
            self.set_right(level, root.val, right)
            self.traverse(root.left, level+1, right)
            self.traverse(root.right, level+1, right)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right = []
        self.traverse(root, 0, right)
        return right
