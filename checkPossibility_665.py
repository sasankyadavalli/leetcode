class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        length = len(nums)
        pos = 0
        flag = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                if flag == 0:
                    flag = 1
                    pos = i
                else:
                    return False
        if flag == 0:
            return True
        if pos == 0 or length == pos + 2:
            return True
        if nums[pos-1] <= nums[pos+1] or nums[pos] <= nums[pos+2]:
            return True
        return False