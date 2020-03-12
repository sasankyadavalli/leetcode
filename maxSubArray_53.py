def maxSubArray(nums):
    curr_max = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        curr_max = max(curr_max + nums[i], nums[i])
        res = max(res, curr_max)

    return res


print(maxSubArray([-3, 8, -2, 4, -5, 6]))