class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = s + t
        xor = 0
        for ele in s:
            xor ^= ord(ele)
            
        return chr(xor)