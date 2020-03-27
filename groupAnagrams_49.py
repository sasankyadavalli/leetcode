class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            a = sorted(string)
            b = ''.join(a)
            if b in d.keys():
                d[b].append(string)
            else:
                d[b] = [string]
                
        return [v for _,v in d.items()]