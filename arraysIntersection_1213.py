class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted([i for i in set(arr1) & set(arr2) & set(arr3)])
