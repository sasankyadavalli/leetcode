class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window_count = 0
        max_count = 0
        v = 'aeiou'
        for i, c in enumerate(s):
            if c in v:
                window_count += 1
            if i >= k and s[i-k] in v:
                window_count -=1
            max_count = max(max_count, window_count)
            
        return max_count