# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
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