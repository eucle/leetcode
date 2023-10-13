def arithmeticTriplets(nums: list[int], diff: int) -> int:
    counter = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] - nums[i] == diff:
                for k in range(j, len(nums)):
                    if nums[k] - nums[j] == diff:
                        counter += 1
    return counter


print(arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))
print(arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))
