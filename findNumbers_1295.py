class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for ele in nums:
            count_temp = 0
            while ele > 0:
                count_temp = count_temp + 1
                ele = ele//10
                
            if count_temp % 2 == 0:
                res = res + 1
            count_temp = 0
        
        return res