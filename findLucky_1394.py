class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        for ele in arr:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1
        
        sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        for k, v in sorted_d.items():
            if k == v:
                return k
            
        return -1