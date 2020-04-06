class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        s_heights = sorted(heights)
        for i in range(len(heights)):
            if(s_heights[i] != heights[i]):
                count += 1 

        return count