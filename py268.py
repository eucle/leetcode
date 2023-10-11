def missingNumber(nums: list[int]) -> int:
    return (set(range(len(nums) + 1)) - set(nums)).pop()
