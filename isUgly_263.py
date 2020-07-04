class Solution:
    def isUgly(self, num: int) -> bool:
        while num > 1:
            if num % 2 == 0:
                num = num // 2
            elif num % 3 == 0:
                num = num // 3
            elif num % 5 == 0:
                num = num // 5

            elif num % 2 != 0 or num % 3 != 0 or num % 5 != 0:
                return False

        return num == 1
        
