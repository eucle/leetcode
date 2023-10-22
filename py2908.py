def minimumSum(nums: list[int]) -> int:
    res = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] < nums[j] and nums[k] < nums[j]:
                    res.append(nums[i] + nums[j] + nums[k])
    return min(res) if res else -1
