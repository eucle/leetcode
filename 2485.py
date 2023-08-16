def pivotInteger(n: int) -> int:
    lst = list(range(1, n + 1))
    for i in range(n):
        if sum(lst[:i]) == sum(lst[i + 1:]):
            return i + 1
    return -1


print(pivotInteger(8))
print(pivotInteger(1))
print(pivotInteger(4))
