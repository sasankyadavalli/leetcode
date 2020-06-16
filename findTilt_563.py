# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        self.tilt(root)
        return self.ans

    def tilt(self, root):
        if not root:
            return 0
        left = self.tilt(root.left)
        right = self.tilt(root.right)

        self.ans += abs(right-left)
        return root.val + left + right
