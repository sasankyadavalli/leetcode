class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_a = 0
        f = 0
        l = len(height)-1
        while f < l:
            max_a = max(max_a, min(height[f], height[l]) * (l-f))
            if height[l] > height [f]:
                f = f+1
            else:
                l = l-1
        
        return max_a