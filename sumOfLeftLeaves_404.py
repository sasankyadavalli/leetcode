class Solution:
    def sumOfLeftLeaves(self, root: TreeNode):
        if root is None:
            return 0
        ans = 0

        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)

        ans += self.sumOfLeftLeaves(root.right)

        return ans
