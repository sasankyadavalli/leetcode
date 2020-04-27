# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))






# Iterative solution:
#         if root is None:
#             return 0
#         stack = []
#         stack.append(root)
#         count = 0
#         while len(stack) > 0:
#             c = len(stack)
#             for i in range(c):
#                 node = stack.pop(0)
#                 if node.left is not None:
#                     stack.append(node.left)
#                 if node.right is not None:
#                     stack.append(node.right)
                    
#             count += 1
            
#         return count