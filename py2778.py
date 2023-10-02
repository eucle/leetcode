def sumOfSquares(nums: list[int]) -> int:
    length = len(nums)
    return sum([v * v for k, v in enumerate(nums, 1) if not length % k])


print(sumOfSquares([1, 2, 3, 4]))
print(sumOfSquares([2, 7, 1, 19, 18, 3]))
