# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        self.result = []
        def dfs(root, res, sum):
            if root.left is None and root.right is None and sum == root.val:
                res.append(root.val)
                self.result.append(res)
            if root.left:
                dfs(root.left, res + [root.val], sum - root.val)
            if root.right:
                dfs(root.right, res + [root.val], sum - root.val)

        dfs(root, [], sum)
        return self.result