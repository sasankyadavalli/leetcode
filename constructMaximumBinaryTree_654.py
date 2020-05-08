# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums:
            ind = nums.index(max(nums))
            root = TreeNode(max(nums))
            root.left = self.constructMaximumBinaryTree(nums[:ind])
            root.right = self.constructMaximumBinaryTree(nums[ind+1:])
            
            return root