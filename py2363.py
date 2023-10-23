def mergeSimilarItems(items1: list[list[int]],
                      items2: list[list[int]]) -> list[list[int]]:
    dct: dict = {}
    items1.extend(items2)
    for i in range(len(items1)):
        dct[items1[i][0]] = dct.get(items1[i][0], 0) + items1[i][1]
    res = [[k, v] for k, v in dct.items()]
    res.sort()
    return res
