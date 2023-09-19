def numberOfPoints(nums: list[list[int]]) -> int:
    res: set = set()
    for i in nums:
        res |= set(range(i[0], i[1] + 1))
    return len(res)
