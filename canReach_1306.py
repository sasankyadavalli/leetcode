class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        return self.helper(arr, start, seen)
    def helper(self, arr, start, seen):
        if start >= len(arr) or start < 0 or (start in seen):
            return False
        if arr[start] == 0:
            return True
        seen.add(start)
        return self.helper(arr, start+arr[start], seen) or self.helper(arr, start-arr[start], seen)