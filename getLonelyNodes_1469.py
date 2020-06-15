# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        def dfs(root, res):
            if root:
                if root.left is None or root.right is None:
                    if root.left:
                        res.append(root.left.val)
                    if root.right:
                        res.append(root.right.val)
                dfs(root.left, res)
                dfs(root.right, res)

        res = []
        dfs(root, res)
        return res
