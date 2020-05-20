class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        rowStart, rowEnd = 0, n-1
        colStart, colEnd = 0, n-1
        count = 1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd+1):
                A[rowStart][i] = count
                count += 1
            rowStart += 1
            for i in range(rowStart, rowEnd+1):
                A[i][colEnd] = count
                count += 1
            colEnd -= 1
            for i in range(colEnd, colStart-1, -1):
                A[rowEnd][i] = count
                count += 1
            rowEnd -= 1
            for i in range(rowEnd, rowStart-1, -1):
                A[i][colStart] = count
                count += 1
            colStart += 1
        return A