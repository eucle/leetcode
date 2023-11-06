def findChampion(grid: list[list[int]]) -> int:
    res = 0
    for i in range(len(grid)):
        if sum(grid[i]) > sum(grid[res]):
            res = i
    return res
