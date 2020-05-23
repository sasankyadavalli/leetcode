class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = {}
        for i in range(len(arr)):
            if arr[i] // 2 in d.values() and arr[i]%2==0:
                return True
            elif arr[i]*2 in d.values():
                return True
            d[i] = arr[i]
            
        return False