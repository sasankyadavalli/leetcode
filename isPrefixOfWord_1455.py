class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        a = len(searchWord)
        print(words)
        for i in range(len(words)):
            if searchWord in words[i][0:a]:
                return i+1
                break
        return -1