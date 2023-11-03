from py2006 import countKDifference


def test_1():
    assert countKDifference([1, 2, 2, 1], 1) == 4


def test_2():
    assert countKDifference([1, 3], 3) == 0


def test_3():
    assert countKDifference([3, 2, 1, 5, 4], 2) == 3
