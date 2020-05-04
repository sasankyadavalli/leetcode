# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        b =[]
        stack = []
        stack.append(root)
        while len(stack) > 0:
            a = len(stack)
            res = []
            for _ in range(a):
                node = stack.pop(0)
                res.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
            
            b.append(res[-1])
            
        return b