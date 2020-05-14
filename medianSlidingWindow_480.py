class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []

        for i in range(len(nums)-k+1):
            window = nums[i:k+i]
            a = sorted(window)
            len_window = len(a)
            if len_window % 2 != 0:
                res.append(a[len_window//2])
            else:
                b = len_window //2
                ele = (a[b] + a[b-1])/2
                res.append(ele)
        return res