class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        count = 0
        for ele in arr:
            if ele in d.keys():
                d[ele] += 1
            else:
                d[ele] = 1
                
        d = sorted(d.items(), key=lambda x:x[1] ,reverse = True)
       
        a = len(arr)
        for k, v in d:
            a -= v
            count += 1
            
            if a <= len(arr)//2:
                break
                
        return count 