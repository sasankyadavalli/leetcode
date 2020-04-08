class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        a = None
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                a = i 
                break
                
        if a is None:
            return nums[0]
                
        b = nums[0:a+1]
        c = nums[a+1:len(nums)]
        
        return min(b[0], c[0])