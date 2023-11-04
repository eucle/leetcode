def countPoints(rings: str) -> int:
    dct: dict = dict()
    for i in range(0, len(rings) - 1, 2):
        dct.setdefault(rings[i + 1], []).append(rings[i])
    return sum(len(set(val)) > 2 for val in dct.values())
