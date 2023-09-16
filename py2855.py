def minimumRightShifts(nums: list[int]) -> int:
    cnt = 0
    sorted_nums = sorted(nums)
    for i in range(len(nums)):
        if nums != sorted_nums:
            nums = [nums.pop(-1)] + nums
            cnt += 1
        else:
            return cnt
    return cnt if nums == sorted_nums else -1
