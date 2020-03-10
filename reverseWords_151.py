class Solution:
    def reverseWords(self, s: str) -> str:
        n = s.split()
        n[:] = n[::-1]
        a = " ".join(n)
        return a