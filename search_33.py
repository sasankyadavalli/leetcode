class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        if len(nums) == 1 and target not in nums:
            return -1
        
        if len(nums) == 1 and target in nums:
            return 0
        
        a = None
        
        
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                a = i
                break
                
        if a is None: 
            return self.binary_search(nums, target)
        
        
        b = nums[0:a+1]
        c = nums[a+1:len(nums)]

        if target >= b[0] and target <= b[-1]:
            if self.binary_search(b, target) == -1:
                return -1
            else:
                return self.binary_search(b, target)

        if target >= c[0]:
            if self.binary_search(c, target) == -1:
                return -1
            else:
                return self.binary_search(c, target) + a + 1
        

        return -1 


    def binary_search(self,arr, target):
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid] == target:
                return mid
            if arr[mid] > target:
                r = r - 1
            else:
                l = l + 1

        return -1

