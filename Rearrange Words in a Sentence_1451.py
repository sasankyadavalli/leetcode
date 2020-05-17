class Solution:
    def arrangeWords(self, text: str) -> str:
        res = []
        arr = text.split(" ")
        for ele in arr:
            ele = ele.lower()
            res.append(ele)
            
        res = sorted(res, key=len)
        res = [res[0].capitalize()]+res[1:]
        print(res)
        return ' '.join(res)