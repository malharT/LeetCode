class Solution:
    def get_list(self, root):
        if root is None:
            return ['#']
        s = [str(root.val)]
        s.extend(self.get_list(root.left))
        s.extend(self.get_list(root.right))
        return s

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        root_s = self.get_list(root)
        sub_s = self.get_list(subRoot)
        if root_s == sub_s:
            return True
        for i in range(len(root_s)-len(sub_s)+1):
            j = 0
            while j < len(sub_s) and sub_s[j]==root_s[i+j]:
                j += 1
            if j==len(sub_s):
                return True
        return False