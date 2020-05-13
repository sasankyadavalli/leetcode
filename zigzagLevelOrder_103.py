# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        stack = []
        stack.append(root)
        count = 0
        while len(stack) > 0:
            a = len(stack)
            b = []
            for _ in range(a):
                node = stack.pop(0)
                b.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)
            if count %2 != 0:
                res.append(b[::-1])
            else:
                res.append(b)
                
            count += 1
            
        return res