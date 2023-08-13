def maxSum(nums: list[int]) -> int:
    res = [nums[i] + nums[j] for i in range(len(nums))
           for j in range(i + 1, len(nums))
           if max(map(int, str(nums[i]))) == max(map(int, str(nums[j])))]
    return max(res) if res else -1


print(maxSum([51, 71, 17, 24, 42]))
print(maxSum([1, 2, 3, 4]))
