def sortByBits(arr: list[int]) -> list[int]:
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
