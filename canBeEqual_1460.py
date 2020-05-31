class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = {}
        for ele in arr:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1
                
        for ele in target:
            if ele in d.keys():
                d[ele] -= 1
            else:
                return False
            
        return True