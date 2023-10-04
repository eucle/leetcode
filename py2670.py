def distinctDifferenceArray(num: list[int]) -> list[int]:
    return [len(set(num[:i+1]))-len(set(num[i+1:])) for i in range(len(num))]


print(distinctDifferenceArray([1, 2, 3, 4, 5]))
print(distinctDifferenceArray([3, 2, 3, 4, 2]))
