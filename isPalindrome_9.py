class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        a = y[::-1]
        if y == a:
            return True
        else:
            False