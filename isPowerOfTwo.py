class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = 1
        while num <= n:
            if n == num:
                return True
            num = num << 1
        
        return False