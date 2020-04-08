class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        a = None
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                a = i
                return nums[i+1]
                break
                
        if a is None:
            return nums[0]