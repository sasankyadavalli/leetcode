class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = start = 0
        d = {}
        for i, st in enumerate(s):
            if st in d and start <= d[st]:
                start = d[st]+1
            else:
                max_len = max(max_len, i-start+1)
            d[st] = i
            
        return max_len


        # i = 0
        # j = 0
        # count = 0
        # count_m = 0
        # while j < len(s):
        #     if s[j] not in s[i:j]:
        #         count_m += 1
        #         j += 1
        #     else:
        #         count = max(count, count_m)
        #         i += 1
        #         j = i
        #         count_m = 0
                
        # return max(count, count_m)