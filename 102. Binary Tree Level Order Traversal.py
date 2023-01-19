# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def add_to_levelorder(self, val, level, levels):
        if level == len(levels):
            levels.append([val])
        else:
            levels[level].append(val)

    def traverse_tree(self, root, level, levels):
        if root is not None:
            self.add_to_levelorder(root.val, level, levels)
            self.traverse_tree(root.left, level+1, levels)
            self.traverse_tree(root.right, level+1, levels)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        self.traverse_tree(root, 0, levels)
        return levels
