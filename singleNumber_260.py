class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d, res = {}, []
        for ele in nums:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1
        for k, v in d.items():
            if v == 1:
                res. append(k)
                
        return res