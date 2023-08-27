def smallestEqual(nums: list[int]) -> int:
    res: list = []
    for i, v in enumerate(nums):
        if i % 10 == v:
            res.append(i)
    return min(res) if res else -1


print(smallestEqual([0, 1, 2]))
print(smallestEqual([4, 3, 2, 1]))
print(smallestEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
