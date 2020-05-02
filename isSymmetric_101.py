# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.isSymmetricBST(root.left, root.right)
    
    def isSymmetricBST(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        elif node1 == None or node2 == None:
            return False
        else:
            return node1.val == node2.val and self.isSymmetricBST(node1.left, node2.right) and self.isSymmetricBST(node1.right, node2.left)