def maximizeSum(nums: list[int], k: int) -> int:
    summ = max(nums)
    return sum([summ + i for i in range(0, k)])


print(maximizeSum([1, 2, 3, 4, 5], 3))
print(maximizeSum([5, 5, 5], 2))
