class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        d = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] in d.keys():
                    d[mat[i][j]] += 1
                else:
                    d[mat[i][j]] = 1
                    
                    
        for k, v in d.items():
            if v == len(mat):
                return k
            
        return -1