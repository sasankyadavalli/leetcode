class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        res = []
        for ele in nums:
            res.append(a.index(ele))
            
        return res