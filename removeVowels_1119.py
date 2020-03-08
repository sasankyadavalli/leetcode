class Solution:
    def removeVowels(self, S: str) -> str:
        s = ""
        for ele in S:
            if ele not in "aeiou":
                s = s + ele
                
        return s