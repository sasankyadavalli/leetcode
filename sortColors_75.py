class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*3
        for ele in nums:
            res[ele] += 1
        
        index = 0
        for i in range(0, len(res)):
            for _ in range(0, res[i]):
                nums[index] = i
                index += 1
                
        return nums