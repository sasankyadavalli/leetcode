# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return root
        c = self.dfs(root, None)
        return c
    def dfs(self, root, prev):
        if root:
            if prev is not None and root.val != prev:
                return False
            else:
                prev = root.val
                return self.dfs(root.left, prev) and self.dfs(root.right, prev)
        else:
            return True