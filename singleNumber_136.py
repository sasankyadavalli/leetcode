class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        return xor
        
        
        # d = {}
        # for ele in nums:
        #     if ele in d.keys():
        #         d[ele] += 1
        #     else:
        #         d[ele] = 1
                
        # for k, v in d.items():
        #     if v % 2 != 0:
        #         return k