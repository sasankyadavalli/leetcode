class Solution:
    def average(self, salary: List[int]) -> float:
        a = sorted(salary)
        b = 0
        count = 0
        for i in range(1, len(a)-1):
            b += a[i]
            count += 1

        return b/count
