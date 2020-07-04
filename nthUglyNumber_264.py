class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i ,j, k = 0, 0, 0
        while n > 1:
            u1, u2, u3 = ugly[i]*2, ugly[j]*3, ugly[k]*5
            minN = min(u1, u2, u3)
            if minN == u1:
                i += 1
            if minN == u2:
                j += 1
            if minN == u3:
                k += 1

            ugly.append(minN)
            n -= 1

        return ugly[-1]
