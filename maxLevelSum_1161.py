# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root is None:
            return root
        res, stack = [], [root]
        while len(stack) > 0:
            a = len(stack)
            b = []
            for _ in range(a):
                node = stack.pop(0)
                b.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
                    
            res.append(sum(b))
            
        a = res.index(max(res))
        
        return a+1