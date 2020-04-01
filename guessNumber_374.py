# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l, r = 1, n

        while l <= r:
            num = (l+r)//2

            if(guess(num) == 0):
                return num

            elif(guess(num) == 1):
                l = num +1
            elif(guess(num) == -1):
                r = num-1
        