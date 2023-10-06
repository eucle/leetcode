def findColumnWidth(grid: list[list[int]]) -> list[int]:
    res = [''] * len(grid[0])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if len(str(grid[i][j])) > len(res[j]):
                res[j] = str(grid[i][j])
    return [len(i) for i in res]


print(findColumnWidth([[1], [22], [333]]))
print(findColumnWidth([[-15, 1, 3], [15, 7, 12], [5, 6, -2]]))
