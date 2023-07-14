def findThePrefixCommonArray(a: list[int], b: list[int]) -> list[int]:
    return [len(set(a[:i]) & set(b[:i])) for i in range(1, len(a) + 1)]


print(findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]))
print(findThePrefixCommonArray([2, 3, 1], [3, 1, 2]))
