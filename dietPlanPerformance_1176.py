class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        count = 0
        window_sum = sum(calories[:k])
        if window_sum < lower:
            count -= 1
        elif window_sum > upper:
            count += 1
            
        for i in range(len(calories)-k):
            window_sum = window_sum - calories[i] + calories[i+k]
            if window_sum < lower:
                count -=1
            elif window_sum > upper:
                count += 1
                
        return count