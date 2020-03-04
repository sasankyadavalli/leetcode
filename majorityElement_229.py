class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        
        res = []
        for k,v in d.items():
            if v > (len(nums))//3:
                res.append(k)
                
        return res