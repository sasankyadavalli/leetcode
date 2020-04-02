class Solution:
    def isHappy(self, n: int) -> bool:
        l = []
        tot = 0
        while n not in l:
            l.append(n)
            while n > 0:
                d = n % 10
                tot += d*d
                n = n // 10
            
            if tot == 1:
                return True
            n = tot
            tot = 0
            
        return False

