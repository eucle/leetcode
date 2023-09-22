def reductionOperations(nums: list[int]) -> int:
    nums.sort(reverse=True)
    return sum(i + 1 for i in range(len(nums) - 1) if nums[i] != nums[i + 1])
