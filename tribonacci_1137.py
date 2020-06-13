class Solution:
    def tribonacci(self, n: int) -> int:
        lookup = [0]*(n+1)
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        lookup[0], lookup[1], lookup[2] = 0, 1, 1
        for i in range(3, n+1):
            lookup[i] = lookup[i-3] + lookup[i-2] + lookup[i-1]
        return lookup[-1]
