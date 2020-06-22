class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                j = i + 1
                while j <= i +k and j < len(nums):
                    if nums[j] == 1:
                        return False
                    else:
                        j += 1

                i = j

            else:
                i += 1

        return True
