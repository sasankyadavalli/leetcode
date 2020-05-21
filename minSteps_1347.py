class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1 = {}
        steps = 0
        for ele in s:
            if ele in d1.keys():
                d1[ele] +=1
            else:
                d1[ele] = 1
        for i in t:
            if i in d1 and d1[i] > 0:
                d1[i] -= 1
            else:
                steps += 1
                
        return steps