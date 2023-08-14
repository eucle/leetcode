def rowAndMaximumOnes(mat: list[list[int]]) -> list[int]:
    maxi, maxi_idx = 0, 0
    for idx, val in enumerate(mat):
        if sum(val) > maxi:
            maxi = sum(val)
            maxi_idx = idx
    return [maxi_idx, maxi]


print(rowAndMaximumOnes([[0, 1], [1, 0]]))
print(rowAndMaximumOnes([[0, 0, 0], [0, 1, 1]]))
print(rowAndMaximumOnes([[0, 0], [1, 1], [0, 0]]))
