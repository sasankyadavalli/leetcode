class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_pr=max_cur = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] < 0:
                max_pr += max_cur
                max_cur = 0
            else:
                max_cur += prices[i] - prices[i-1]
                
        return max_pr+max_cur