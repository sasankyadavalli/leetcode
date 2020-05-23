class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        i, res = 0, []
        perm = [i for i in range(1,m+1)]
        while i < len(queries):
            a = perm.index(queries[i])
            res.append(a)
            b = perm.pop(a)
            perm = [b] + perm
            i += 1
            
        return res