class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l_count = r_count = w_count = 0
        for ele in s:
            if ele == 'L':
                l_count += 1
            else:
                r_count += 1
            if l_count == r_count:
                w_count += 1
                
        return w_count