def countKDifference(nums: list[int], k: int) -> int:
    ln = len(nums)
    return sum(abs(nums[i] - nums[j]) == k
               for i in range(ln-1) for j in range(i, ln))
