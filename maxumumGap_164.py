class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        a = sorted(nums)
        print(a)
        i, j, d = 0, 1, float("-inf")
        while j < len(a):
            d = max((a[j]-a[i]), d)
            i += 1
            j += 1
            
        return d