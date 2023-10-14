def dominantIndex(nums: list[int]) -> int:
    sorted_nums = sorted(nums)
    if sorted_nums[-2] and sorted_nums[-1] / sorted_nums[-2] < 2:
        return -1
    return nums.index(sorted_nums[-1])
