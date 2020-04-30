# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:            
        r = []
        if root is None:
            return []
        self.dfs(root, '', r)
        return r
    
    def dfs(self, root, s, res):
        if root.left is None and root.right is None:
            res.append(s + str(root.val))
        if root.left:
            self.dfs(root.left, s + str(root.val) + '->', res)
        if root.right:
            self.dfs(root.right, s + str(root.val) + '->', res)
            
        return res