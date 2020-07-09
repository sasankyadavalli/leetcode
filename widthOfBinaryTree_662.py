# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        stack = []
        stack.append((root, 1))
        ans = 0
        while stack:
            stack_len = len(stack)
            ans = max(ans, stack[-1][1] - stack[0][1]+1)

            for _ in range(stack_len):
                node, pos = stack.pop(0)
                if node.left:
                    stack.append((node.left, 2*pos))
                if node.right:
                    stack.append((node.right, 2*pos + 1))


        return ans
