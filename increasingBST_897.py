# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        res = self.inorder(root, [])
        
        root = cur = TreeNode(res[0])
        for i in range(1, len(res)):
            cur.right = TreeNode(res[i])
            cur = cur.right
        
        return root
    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
            
        return res