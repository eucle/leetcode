def sumOfUnique(nums: list[int]) -> int:
    dictio: dict = {}
    for num in nums:
        dictio[num] = dictio.get(num, 0) + 1
    return sum([k for k, v in dictio.items() if v < 2])


print(sumOfUnique([1, 2, 3, 2]))
print(sumOfUnique([1, 1, 1, 1, 1]))
print(sumOfUnique([1, 2, 3, 4, 5]))
