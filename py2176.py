def countPairs(nums: list[int], k: int) -> int:
    counter = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and not (i * j) % k:
                counter += 1
    return counter


print(countPairs([3, 1, 2, 2, 2, 1, 3], 2))
print(countPairs([1, 2, 3, 4], 1))
