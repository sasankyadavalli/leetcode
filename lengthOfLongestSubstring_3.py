class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        count = 0
        count_m = 0
        while j < len(s):
            if s[j] not in s[i:j]:
                count_m += 1
                j += 1
            else:
                count = max(count, count_m)
                i += 1
                j = i
                count_m = 0
                
        return max(count, count_m)