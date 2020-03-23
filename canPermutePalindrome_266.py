class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}
        for ele in s:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1
                
        if len(s)%2 == 0:
            for _,v in d.items():
                if v%2 != 0:
                    return False
            return True
        else:
            res = []
            for _,v in d.items():
                if v%2!= 0:
                    res.append(v)
                    
            if len(res) == 1:
                return True
            else:
                return False