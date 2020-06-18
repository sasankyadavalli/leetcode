class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(0, n):
            for j in range(0, m):
                if (i== 0 or j == 0):
                    grid[i][j] = 1
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[-1][-1]
