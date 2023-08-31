def countDistinctIntegers(nums: list[int]) -> int:
    for i in range(len(nums)):
        nums.append(int(str(nums[i])[::-1]))
    return len(set(nums))


print(countDistinctIntegers([1, 13, 10, 12, 31]))
print(countDistinctIntegers([2, 2, 2]))
