# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root1 is None:
            return True
        if root1 is None or root2 is None:
            return False
        
        res1 = self.leaves(root1, [])
        res2 = self.leaves(root2, [])
        
        if res1 == res2:
            return True
        else:
            return False
    
    def leaves(self, root, res):
        if root:
            self.leaves(root.left, res)
            if root.left is None and root.right is None:
                res.append(root.val)
            self.leaves(root.right, res)
            
        return res