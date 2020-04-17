class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        s = 0
        while n > 0:
            digit = n % 10 
            n = n // 10
            product = product * digit
            s = s + digit
            
        return product - s