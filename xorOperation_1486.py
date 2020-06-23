class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x = 0
        while n > 0:
            x ^= start
            start += 2
            n -= 1

        return x
