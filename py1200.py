def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    arr.sort()
    diff, res = arr[1] - arr[0], []
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] < diff:
            diff = arr[i + 1] - arr[i]
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == diff:
            res.append([arr[i], arr[i + 1]])
    return res
