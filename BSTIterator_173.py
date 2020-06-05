class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = [] 
        def inorder(root):
            if root:
                inorder(root.left)
                self.res.append(root.val)
                inorder(root.right)
        
        inorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if len(self.res) > 0:
            return self.res.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.res) > 0:
            return True
        else:
            return False