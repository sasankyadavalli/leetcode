class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2 = sorted(arr2)
        count = 0
        for n in arr1:
            mid = bisect.bisect(arr2,n)
            if (0<=mid<len(arr2) and abs(arr2[mid]-n)<=d) or (0<=mid-1<len(arr2) and abs(arr2[mid-1]-n)<=d):
                continue
            else:
                count+=1
        return count
