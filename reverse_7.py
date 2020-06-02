class Solution:
    def reverse(self, x: int) -> int:
        new = 0
        sign = True
        if x < 0:
            sign = False
            x = -1*x
        a = len(str(x))
        count = a-1
        while count >= 0:
            if x % 10 == 0:
                count -= 1
                x = x // 10
            else:
                break
        while count >= 0:
            num = x % 10
            new += num * 10**count
            x = x // 10
            count -= 1
            
        if new > pow(2, 31):
            return 0
            
        if sign == False:
            return -1 * new
            
        else:
            return new