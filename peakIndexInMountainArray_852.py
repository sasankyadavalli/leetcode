class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        
        while 1 > 0:
            i = (l+r)//2
            
            if(A[i-1] < A[i] > A[i+1]):
                return i
            elif(A[i-1] < A[i] < A[i+1]):
                l = i+1
            else:
                r = i-1