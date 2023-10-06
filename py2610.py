def findMatrix(nums: list[int]) -> list[set[int]]:
    res = []
    while nums:
        row = set(nums)
        for i in row:
            nums.remove(i)
        res.append(row)
    return res


print(findMatrix([1, 3, 4, 1, 2, 3, 1]))
print(findMatrix([1, 2, 3, 4]))
