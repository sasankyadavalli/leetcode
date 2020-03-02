class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        sell = 0
        while j < len(prices) and i < len(prices):
            if prices[i] >= prices[j]:
                i = j
                j = j + 1
                
            else:
                sell = max(sell, (prices[j]-prices[i]))
                j = j + 1
        return sell