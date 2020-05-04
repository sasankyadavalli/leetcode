# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
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
                    
                    
            res.append(max(a))
            
            
        return res