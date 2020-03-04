class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, h = 1, num//2
        while l <= h:
            mid = (l+h)//2
            square = mid ** 2
            if square == num:
                return True
            elif square > num:
                h = mid - 1
            else:
                l = mid + 1
        return False