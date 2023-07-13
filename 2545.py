def sortTheStudents(score: list[list[int]], k: int) -> list[list[int]]:
    return sorted(score, key=lambda x: x[k], reverse=True)


print(sortTheStudents([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2))
print(sortTheStudents([[3, 4], [5, 6]], 0))
