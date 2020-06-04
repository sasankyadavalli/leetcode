class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        idx1 = float('inf')
        idx2 = float('inf')
        shortest = float('inf')
        for i, word in enumerate(words):
            if word1 == word2 == word:
                # idx1 was updated at time t
                # idx2 was updated at time h
                # if h is earlier than t, we update idx2
                # if t is earlier than h, we update idx1
                if idx1 == float('inf'):
                    idx1 = i
                elif idx2 == float('inf'):
                    idx2 = i
                elif idx1 <= idx2:
                    idx1 = i
                else:
                    idx2 = i
                shortest = min(shortest, abs(idx1 - idx2))    
            elif word1 == word:
                idx1 = i
                shortest = min(shortest, abs(idx1 - idx2))
            elif word2 == word:
                idx2 = i
                shortest = min(shortest, abs(idx1 - idx2))
        return shortest