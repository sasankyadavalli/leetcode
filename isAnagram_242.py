class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == "":
            return True
        else:
            d = {}
            for ele in s:
                if ele in d.keys():
                    d[ele] += 1
                else:
                    d[ele] = 1

            for ele in t:
                if ele in d.keys():
                    d[ele] -= 1
                else:
                    return False
            
            for _,v in d.items():
                if v != 0:
                    return False
            return True