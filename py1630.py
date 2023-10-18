def checkArithmeticSubarrays(nums: list[int], le: list[int],
                             r: list[int]) -> list[bool]:
    cnt: set = set()
    res: list = []
    for i in range(len(le)):
        sel_nums = sorted(nums[le[i]:r[i] + 1])
        for j in range(len(sel_nums) - 1):
            cnt.add(sel_nums[j + 1] - sel_nums[j])
        if len(cnt) == 1:
            res.append(True)
        else:
            res.append(False)
        cnt.clear()
    return res
