# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_traversal(self, node, ans):
        if node is None:
            return ans
        if node.left is not None:
            self.inorder_traversal(node.left, ans)
        ans += [node.val]
        if node.right is not None:
            self.inorder_traversal(node.right, ans)
        return ans
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder_traversal(root, [])