# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.d = {}
        self.res = []
        self.serial(root)
        return self.res

    def serial(self, root):
        if not root:
            return '*'
        path = self.serial(root.left) +self.serial(root.right)  + str(root.val)
        count = self.d.get(path, 0)
        if count == 1:
            self.res.append(root)
        self.d[path] = count + 1
        return path
