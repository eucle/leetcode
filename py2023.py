def numOfPairs(nums: list[str], target: str) -> int:
    return sum(nums[i] + nums[j] == target for i in range(len(nums))
               for j in range(len(nums)) if i != j)


print(numOfPairs(["777", "7", "77", "77"], "7777"))
print(numOfPairs(["123", "4", "12", "34"], "1234"))
print(numOfPairs(["1", "1", "1"], "11"))
