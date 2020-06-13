class Solution:
    def climbStairs(self, n):
        lookup = [0]*(n+1)
        if n == 1: return 1
        if n == 2; return 2
        lookup[1], lookup[2] = 1, 2
        for i in range(3, n+1):
            lookup[i] = lookup[i-2] + lookup[i-1]

        return lookup[-1] 
