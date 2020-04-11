class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s)-1
        vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        c = list(s)
        while i < j:
            if c[i] in vow and c[j] in vow:
                c[i], c[j] = c[j], c[i]
                i += 1
                j -= 1
            elif c[i] in vow and c[j] not in vow:
                j -= 1
            elif c[j] in vow and c[i] not in vow:
                i += 1
            elif c[i] and c[j] not in vow:
                i += 1
                j -= 1
        
        
        return "".join(c)