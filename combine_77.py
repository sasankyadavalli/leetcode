class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res, self.k = [], k
        self.dfs(1, [], n)
        return self.res

    def dfs(self, first, path, n):
        if len(path) == self.k:
            self.res.append(path)
            return
        for i in range(first, n+1):
            self.dfs(i+1, path+[i], n)
