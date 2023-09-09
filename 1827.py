def minOperations(nums: list[int]) -> int:
    res = 0
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            res += nums[i - 1] - nums[i] + 1
            nums[i] += nums[i - 1] - nums[i] + 1
    return res


print(minOperations([1, 5, 2, 4, 1]))
