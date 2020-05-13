class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        if len(S) < K:
            return 0
        count = 0
        window = S[:K]
        if len(window) == len(set(window)):
            count += 1
        for i in range(1, len(S)-K+1):
            window = S[i:K+i]
            if len(window) == len(set(window)):
                count += 1
                
        return count