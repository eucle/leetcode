def getSmallestString(n: int, k: int) -> str:
    res = []
    for i in range(n):
        x = 1
        while k - x - (n - i - 1) != 0 and x != 26:
            x += 1
        k -= x
        res.append(chr(x + 96))
    return ''.join(reversed(res))
