class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for ele in s:
            if ord(ele) in d.keys():
                d[ord(ele)] += 1
            else:
                d[ord(ele)] = 1
                
        # for k, v in d.items():
        #     if v % 2 == 0:
        #         return len(s)
        res = []
        count = 0
        for k, v in d.items():
            if v%2 == 0:
                count = count + v
            else:
                res.append(v)
                
        if res == []:
            return count
                
        else:
            for ele in res:
                count = count + ele - 1
                
            return count+1