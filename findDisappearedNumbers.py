class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        temp = [0]*(len(nums)+1)
        for i in range(len(nums)):
            temp[nums[i]] = 1
        
        result = []
        for i in range(1, len(nums)+1):
            if temp[i] == 0:
                result.append(i)
                
        return result