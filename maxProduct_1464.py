class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = nums[0]
        second_max = 0
        
        for i in range(1,len(nums)):
            if nums[i]>=max_val:
                second_max = max_val
                max_val = nums[i]
            elif nums[i]>second_max:
                second_max = nums[i]
        
        return (max_val-1)*(second_max-1)
        # nums.sort()
        # return (nums[-1]-1)*(nums[-2]-1)
#         m = float("-inf")
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 m = max(m, ((nums[i]-1) * (nums[j]-1)))
                
#         return m