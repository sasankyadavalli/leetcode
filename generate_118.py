class Solution:
    def generate(self, n: int) -> List[List[int]]:
        result, pend = [], [1]
        for i in range(n):
            result.append(pend)
            pend = [1] + [pend[k] + pend[k+1] for k in range(len(pend) - 1)] + [1]
        return result
