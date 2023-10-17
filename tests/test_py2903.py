from py2903 import findIndices


def test_1():
    assert findIndices([5, 1, 4, 1], 2, 4) == [0, 3]


def test_2():
    assert findIndices([2, 1], 0, 0) == [0, 0]


def test_3():
    assert findIndices([1, 2, 3], 2, 4) == [-1, -1]
