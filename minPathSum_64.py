class Solution:
    def minPathSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return sum(mat[0])
        for i in range(len(mat)-1):
            for j in range(len(mat[i])-1):
                if j == 0:
                    mat[i+1][0] += mat[i][0]
                if i == 0:
                    mat[0][j+1] += mat[0][j]

        for i in range(1, len(mat)):
            for j in range(1, len(mat[i])):
                mat[i][j] = mat[i][j] + min(mat[i-1][j], mat[i][j-1])

        return mat[-1][-1]
