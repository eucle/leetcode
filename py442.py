def findDuplicates(nums: list[int]) -> list[int]:
    set_nums, res = set(), []
    for num in nums:
        if num in set_nums:
            res.append(num)
        else:
            set_nums.add(num)
    return res
