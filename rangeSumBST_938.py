# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Not an efficient solution
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int: 
        res = []
        q = []
        count = 0
        q.append(root)
        while len(q) > 0:
            node = q.pop(0)
            res.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
                
        for ele in res:
            if ele >= L and ele <= R:
                count = count + ele
                
        return count