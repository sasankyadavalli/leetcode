# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.m = 0
        return self.reverse_inorder(root)
    
    def reverse_inorder(self, root):
        if root is None:
            return
        else:
            self.reverse_inorder(root.right)
            self.m += root.val
            root.val = self.m
            self.reverse_inorder(root.left)
            return root