# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        m = float("inf")
        n = root.val
        return self.dfs(root, target, m, n)
    
    def dfs(self, root, target, m, n):
        if root:
            if abs(root.val - target) < m:
                m = abs(root.val - target)
                n = root.val
            if root.val > target:
                return self.dfs(root.left, target, m, n)
            elif root.val  <  target:
                return self.dfs(root.right, target, m, n)
            
        return n