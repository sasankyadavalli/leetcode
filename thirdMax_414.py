class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = sorted(nums)
        count = 0
        print(a)
        for i in range(len(a)-1, 0, -1):
            if a[i] != a[i-1]:
                count += 1
                
            if count == 2:
                return a[i-1]
            
        return a[-1]