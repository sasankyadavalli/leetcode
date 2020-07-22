class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for ele in arr:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1

        return len(d.values()) == len(set(d.values()))
