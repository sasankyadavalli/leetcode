class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one, two = 0, 0
        for i in nums:
            one, two, three = one^i, two | (one & i), two&i
            one, two = one & ~three, two & ~three
            
        return one