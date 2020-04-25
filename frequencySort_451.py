class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ele in s:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1

        a = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

        s =""
        for k, v in a.items():
            s = s + (k*v)

        return s
