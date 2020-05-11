# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root, sum):
            if not root:
                return 0
            sum = sum*10 + root.val
            if not root.left and not root.right:
                return sum
            return helper(root.left, sum) + helper(root.right, sum)
        
        return helper(root, 0)

