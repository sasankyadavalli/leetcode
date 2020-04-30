# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        res = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            c = len(stack)
            a = []
            for _ in range(c):
                node = stack.pop(0)
                a.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
                    
            res.append(a)
            
        return sum(res[-1])