# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        path = []
        self.count = 0
        def paths(root, path):
            if root.left is None and root.right is None:
                if checkPalindrome(path+[root.val]):
                    self.count += 1
            if root.left:
                paths(root.left, path + [root.val])
            if root.right:
                paths(root.right, path + [root.val])
                
        def checkPalindrome(arr):
            odd = 0
            d = {}
            for ele in arr:
                if ele in d.keys():
                    d[ele] += 1
                else:
                    d[ele] = 1
                    
            for k, v in d.items():
                if v%2 != 0:
                    odd += 1
                    
                if odd > 1:
                    return False
            return True
        
        paths(root, path)
        return self.count