class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        l, r = 0, len(nums)
        def dfs(nums, l, r):
            if l == r:
                res.append(nums[:])
            else:
                for i in range(l, r):
                    nums[l], nums[i] = nums[i], nums[l]
                    dfs(nums, l+1, r)
                    nums[l], nums[i] = nums[i], nums[l]
                    
        dfs(nums, l, r)
        return res