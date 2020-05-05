# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        
        hs = set()
        
        self.left_dfs(root1, hs, target)
        return self.right_dfs(root2, hs)
        
            
        
    def left_dfs(self, root, hs, target):
        if root:
            self.left_dfs(root.left, hs, target)
            hs.add(target - root.val)
            self.left_dfs(root.right, hs, target)
            
        return hs
    
    def right_dfs(self, root, hs):
        if root:
            if root.val in hs:
                return True
            left = self.right_dfs(root.left, hs)
            right = self.right_dfs(root.right, hs)
            
            return left or right