class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not target in nums:
            return [-1, -1]
        l, h = 0, len(nums)
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                a = mid
                b = mid
                while a > 0:
                    if nums[a] == nums[a-1]:
                        a -= 1
                    else:
                        break
                while b < len(nums)-1:
                    if nums[b] == nums[b+1]:
                        b += 1
                    else:
                        break
                return [a,b]
            if nums[mid] > target:
                h = mid
            else:
                l = mid
                
        return [-1, -1]