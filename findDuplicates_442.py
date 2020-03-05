class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for ele in nums:
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1
        
        res = []
        for k,v in d.items():
            if v == 2:
                res.append(k)
                
        return sorted(res) 