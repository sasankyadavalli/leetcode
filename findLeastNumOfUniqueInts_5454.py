from collections import Counter
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = 0
        val = Counter(arr)
        sorted_val = {k: v for k, v in sorted(val.items(), key=lambda item: item[1])}
        print(sorted_val)
        for key, val in sorted_val.items():
            while k > 0:
                if sorted_val[key] == 0:
                    break
                sorted_val[key] -= 1
                k -= 1


        for k, v in sorted_val.items():
            if v != 0:
                count += 1

        return count
