class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min, ans = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            temp = cur_max
            cur_max = max(n, n*cur_max, n*cur_min)
            cur_min = min(n, n*temp, n*cur_min)
            ans = max(ans, cur_max)
        return ans