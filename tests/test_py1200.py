from py1200 import minimumAbsDifference


def test_1():
    res = [[1, 2], [2, 3], [3, 4]]
    assert minimumAbsDifference([4, 2, 1, 3]) == res


def test_2():
    inp = [3, 8, -10, 23, 19, -4, -14, 27]
    res = [[-14, -10], [19, 23], [23, 27]]
    assert minimumAbsDifference(inp) == res
