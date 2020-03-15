# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #Write your code here
        stack = []
        res = []
        while root or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                temp = stack[-1].right
                if temp is not None:
                    root = temp
                else:
                    temp = stack.pop()
                    res.append(temp.val)
                    while(len(stack)!= 0 and stack[-1].right == temp):
                        temp = stack.pop()
                        res.append(temp.val)
        return res                