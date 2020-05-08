# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        
        return self.dfs(root, set(), k)
        
    def dfs(self, root, nodes, k):
        if not root:
            return False
        
        c = k - root.val
        if c in nodes:
            return True
        
        nodes.add(root.val)
        
        return self.dfs(root.left, nodes,k) or self.dfs(root.right, nodes, k)

