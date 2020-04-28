# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        stack = []
        stack.append(root)
        res = []
        while len(stack) > 0:
            c = len(stack)
            a = []
            for i in range(c):
                node = stack.pop(0)
                a.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
                    
            res.append(a)
            
        return res[-1][0]