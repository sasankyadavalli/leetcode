class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = 0
        j = 1
        while j < len(A):
            if A[j] % 2 == 0:    
                A[j], A[i] = A[i], A[j]
                i += 2                         
            else:
                j += 2
        return A