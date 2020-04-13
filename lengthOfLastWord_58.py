class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if(len(s.split()) < 1):
            return 0
        else:
            return len(s.split()[-1])