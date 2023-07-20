def generate(numRows: int) -> list[list[int]]:
    triangle: list = [[1]]
    for i in range(numRows - 1):
        row = [1]
        for j in range(1, i + 1):
            row += [sum(triangle[i][j - 1:j + 1])]
        row += [1]
        triangle.append(row)
    return triangle


print(generate(5))
print(generate(1))
