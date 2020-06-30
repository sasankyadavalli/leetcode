class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        result = [None]*len(A)
        for i in range(len(B)):
            index = B.index(A[i])
            result[i] = index
            B[index] = None
        return result 
