# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left is None and root.right is None:
            return [str(root.val)]
        elif root.right is None:
            all_paths = self.binaryTreePaths(root.left) 
        elif root.left is None:
            all_paths = self.binaryTreePaths(root.right)
        else:
            all_paths = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        for i in range(len(all_paths)):
            all_paths[i] = str(root.val) + "->" + all_paths[i]
        return all_paths