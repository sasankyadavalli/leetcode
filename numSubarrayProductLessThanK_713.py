class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start, prod = 0, 1
        res = 0
        for i, n in enumerate(nums):
            prod *= n
            while prod >= k and start <= i:
                prod //= nums[start]
                start += 1
            res += i - start + 1

        return res
