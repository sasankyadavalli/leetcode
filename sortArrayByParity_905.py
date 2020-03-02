class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) == 1:
            return A
        else:
            i = 0
            j = 1
            while j < len(A):
                if A[i] % 2 != 0 and A[j] % 2 != 0:
                    j+= 1
                elif A[i] % 2 !=0 and A[j] % 2 == 0:
                    A[i], A[j] = A[j], A[i]
                    i += 1
                    j += 1
                    
                elif A[i] % 2 == 0 and A[j] %2 == 0:
                    i += 1
                    j += 1
                    
                elif A[i] % 2 == 0 and A[j] %2 != 0:
                    i += 1
                    j += 1
                    
            return A