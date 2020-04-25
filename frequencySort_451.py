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
            b = v
            while b > 0:
                s = s + k
                b -= 1

        return s
