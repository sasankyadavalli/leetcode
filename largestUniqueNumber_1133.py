class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        d = {}
        for ele in A:
            if ele in d.keys():
                d[ele] += 1
            else:
                 d[ele] = 1
                    
        
        a = float("-inf")
        for k, v in d.items():
            if v == 1:
                a = max(k, a)
                
        if a == float("-inf"):
            return -1
        else:
            return a