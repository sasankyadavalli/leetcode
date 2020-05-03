# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        res = []
        s = []
        a = self.dfs(root, s, res, arr)
        
        if arr in a:
            return True
        else:
            return False
    def dfs(self, root, s, res, arr):
        if root.left is None and root.right is None:
            s = s + [root.val]
            res.append(s)
        if root.left:
            self.dfs(root.left, s + [root.val], res, arr)
        if root.right:
            self.dfs(root.right, s + [root.val], res, arr)
            
        return res