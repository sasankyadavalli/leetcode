class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 1
        for i in range(1, n+1):
            if n % i == 0 and count != k:
                count += 1

            elif n%i == 0 and count == k:
                return i

        return -1
