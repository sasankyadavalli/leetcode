class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word1_ind = None
        word2_ind = None
        dist = float("inf")
        for i in range(len(words)):
            if words[i] == word1:
                word1_ind = i
            elif words[i] == word2:
                word2_ind = i
            if word1_ind != None and word2_ind != None:
                dist = min(dist, abs(word2_ind - word1_ind))
                
        return dist