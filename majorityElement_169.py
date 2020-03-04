from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        v = max(c.values())
        for k,val in c.items():
            if val == v:
                return k