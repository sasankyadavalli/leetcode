class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return root

        stack = []
        res = []
        stack.append(root)
        while len(stack) > 0:
            c = len(stack)
            a = []
            for i in range(0, len(stack)):
                node = stack.pop(0)
                a.append(node.val)
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)

            res.append(a)

        return res[::-1]
