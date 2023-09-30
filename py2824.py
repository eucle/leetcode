def countPairs(nums: list[int], target: int) -> int:
    return sum([(nums[i]+nums[j] <
                 target) for i in range(len(nums)-1) for j in range(i+1, len(nums))])


print(countPairs(nums=[-1, 1, 2, 3, 1], target=2))
print(countPairs(nums=[-6, 2, 5, -2, -7, -1, 3], target=-2))
