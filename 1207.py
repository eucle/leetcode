def uniqueOccurrences(arr: list[int]) -> bool:
    dictio: dict = {}
    for num in arr:
        dictio[num] = dictio.get(num, 0) + 1
    return len(set(dictio.keys())) == len(set(dictio.values()))


print(uniqueOccurrences([1, 2, 2, 1, 1, 3]))
print(uniqueOccurrences([1, 2]))
print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
