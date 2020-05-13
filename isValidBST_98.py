# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.flag = True
        self.inOrder(root, [])
        return self.flag
    
    def inOrder(self, root, res):
        if root:
            self.inOrder(root.left, res)
            if res and root.val <= res[-1]:
                self.flag = False
                return
            res.append(root.val)
            self.inOrder(root.right, res)
# ---------------------------------------------------------------
#         if root is None:
#             return True
#         res = self.inOrder(root, [])
        
#         for i in range(len(res)-1):
#             if res[i] >= res[i+1]:
#                 return False
#         return True
#     def inOrder(self, root, res):
#         if root:
#             self.inOrder(root.left, res)
#             res.append(root.val)
#             self.inOrder(root.right, res)
#         return res