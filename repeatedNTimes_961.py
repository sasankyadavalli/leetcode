from collections import Counter
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        new_list = []
        for ele in A:
            if ele in new_list:
                return ele
            
            new_list.append(ele)