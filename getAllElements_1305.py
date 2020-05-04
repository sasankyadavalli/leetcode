class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res1 = []
        res2 = []
        if root1 is None:
            return sorted(self.preorder(root2, res2))
        if root2 is None:
            return sorted(self.preorder(root1, res1))
        
        r1 = self.preorder(root1, res1)
        r2 = self.preorder(root2, res2)
        
        r1 = sorted(r1 + r2)
        return r1
        
        
    
    def preorder(self, root, res):
        if root:
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)
            
        return res