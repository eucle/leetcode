def largestLocal(grid: list[list[int]]) -> list[list[int]]:
    res = []
    for x in range(len(grid) - 2):
        inside_res = []
        for y in range(len(grid) - 2):
            max_num = 0
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    if max_num < grid[i][j]:
                        max_num = grid[i][j]
            inside_res.append(max_num)
        res.append(inside_res)
    return res


print(largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
print(largestLocal([[1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 2, 1, 1],
                    [1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1]]))
