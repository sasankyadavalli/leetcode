class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for ele in s:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1
                
        for k, v in d.items():
            if v == 1:
                return s.index(k)
        return -1