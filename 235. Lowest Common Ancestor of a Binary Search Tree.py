# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def LCA(self, root, p, q):
        if p.val > root.val:
            return self.lowestCommonAncestor(root.right, p ,q)
        elif q.val < root.val:
            return self.lowestCommonAncestor(root.left, p ,q)
        elif (p.val < root.val and q.val > root.val) or p.val==root.val or q.val==root.val:
            return root
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if q.val < p.val:
            temp = p
            p = q
            q = temp
        return self.LCA(root, p, q)
