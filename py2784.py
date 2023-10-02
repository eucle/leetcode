def isGood(nums: list[int]) -> bool:
    res = list(set(nums))
    res.append(max(nums))
    res.sort()
    nums.sort()
    return res == nums if len(nums) == max(nums) + 1 else False


print(isGood([2, 1, 3]))
print(isGood([1, 3, 3, 2]))
print(isGood([1, 1]))
print(isGood([3, 4, 4, 1, 2, 1]))
