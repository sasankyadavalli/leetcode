# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        su = []
        if root is None:
            return 0
        self.dfs(root, '',su)
        return sum(su)
        
    def dfs(self, root, s, su):
        if root.left is None and root.right is None:
            su.append(int(s + str(root.val), 2))
        if root.left:
            self.dfs(root.left, s+str(root.val), su)
        if root.right:
            self.dfs(root.right, s+str(root.val), su)