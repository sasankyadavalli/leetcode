from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        count_s1 = Counter(s1)

        window = None
        for i in range(len_s2-len_s1+ 1):
            if i == 0:
                window = Counter(s2[:len_s1])
            else:
                window[s2[i-1]] -= 1
                window[s2[i+len_s1-1]] += 1

            if len(window - count_s1) == 0:
                return True

        return False
