# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        l, r = root.left, root.right
        root.left, root.right = None, root.left
        self.flatten(l)
        while root.right:
            root = root.right
        root.right = r
        self.flatten(r)
        return root
    # ====================================================
    # Two Iterations
    #     if root is None:
    #         return root
    #     res = []
    #     r = self.preOrder(root, res)
    #     root = cur = res[0]
    #     for i in range(1, len(res)):
    #         cur.left = None
    #         cur.right = res[i]
    #         cur = cur.right
    #     return root
        
    # def preOrder(self, root, res):
    #     if root:
    #         res.append(root)
    #         self.preOrder(root.left, res)
    #         self.preOrder(root.right, res)
    #     return res