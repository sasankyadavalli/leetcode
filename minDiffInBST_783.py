# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []
        def inorder(root, res):
            if root:
                inorder(root.left, res)
                res.append(root.val) 
                inorder(root.right, res)
            return res
        inorder(root, res)
        return min(abs(res[i+1])-res[i] for i in range(len(res)-1))