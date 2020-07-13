class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        good_pairs = 0
        for count in counts.values():
            if count > 1:
                good_pairs += count * (count - 1) // 2
        return good_pairs
