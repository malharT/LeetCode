# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder[0])
        part_idx = inorder.index(preorder[0])
        if part_idx > 0:
            root.left = self.buildTree(preorder[1:part_idx+1], inorder[:part_idx])
        if part_idx + 1 < len(inorder):
            root.right = self.buildTree(preorder[part_idx+1:], inorder[part_idx+1:])
        return root