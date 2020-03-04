class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        d = {}
        for ele in nums:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1
                
        for k, v in d.items():
            if k == target and v > (len(nums))//2:
                return True
            
        return False