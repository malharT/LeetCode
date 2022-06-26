class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def gen_trees(self, nums, root_val=None, tree=None):
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [TreeNode(val=nums[0])]

        solution = []
        for i in range(len(nums)):
            if tree is not None and tree == 'l':
                if nums[i] > root_val:
                    continue
            if tree is not None and tree == 'r':
                if nums[i] < root_val:
                    continue
            num = nums[i]
            new_nums = (list(nums))
            del new_nums[i]

            split_i = min(i, len(new_nums))
            if len(new_nums[:split_i]) > 0 and len(new_nums[split_i:]) > 0:
                lef_array = new_nums[:split_i]
                rig_array = new_nums[split_i:]
                trees_on_left = self.gen_trees(lef_array, root_val=num, tree='l')
                if len(lef_array) > 0:
                    if len(trees_on_left) == 0:
                        continue
                trees_on_right = self.gen_trees(rig_array, root_val=num, tree='r')
                if len(rig_array) > 0:
                    if len(trees_on_right) == 0:
                        continue
                if len(trees_on_left)>0 and len(trees_on_right)>0:
                    for tree_l in trees_on_left:
                        for tree_r in trees_on_right:
                            node = TreeNode(val=num)
                            node.left = tree_l
                            node.right = tree_r
                            solution.append(node)
                elif len(trees_on_left) > 0:
                    for tree_l in trees_on_left:
                        node = TreeNode(val=num)
                        node.left = tree_l
                        solution.append(node)
                elif len(trees_on_right) > 0:
                    for tree_r in trees_on_right:
                        node = TreeNode(val=num)
                        node.right = tree_r
                        solution.append(node)

            elif len(new_nums[:split_i]) > 0:
                lef_array = new_nums[:split_i]
                trees_on_left = self.gen_trees(lef_array, root_val=num, tree='l')
                for tree_l in trees_on_left:
                    node = TreeNode(val=num)
                    node.left = tree_l
                    solution.append(node)
            else:
                rig_array = new_nums[split_i:]
                trees_on_right = self.gen_trees(rig_array, root_val=num, tree='r')
                for tree_r in trees_on_right:
                    node = TreeNode(val=num)
                    node.right = tree_r
                    solution.append(node)
        return solution

    def generateTrees(self, n: int):
        return self.gen_trees(list(range(1, n+1)))

s = Solution()
def preorder(tree):
    if tree:
        print(tree.val, end=' ')
        preorder(tree.left)
        preorder(tree.right)
    else:
        print('null', end=' ')
for tree in s.generateTrees(8):
    preorder(tree)
    print()