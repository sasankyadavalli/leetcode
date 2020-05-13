class Solution:
    def countElements(self, arr: List[int]) -> int:
        hash_set = set(arr)
        count = 0
        for ele in arr:
            if ele+1 in hash_set:
                count += 1
            hash_set.add(ele)
                
        return count