def sumCounts(nums: list[int]) -> int:
    res: list = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            res.append(pow(len(set(nums[i:j])), 2))
    return sum(res)
