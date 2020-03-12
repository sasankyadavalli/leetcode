class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_arr = []
        for i in range(0, len(nums)):
            if(i+k <= (len(nums))):
                max_arr.append(max(nums[i:i+k]))
                
        return max_arr