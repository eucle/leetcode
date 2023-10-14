from py747 import dominantIndex


def test_1():
    assert dominantIndex([3, 6, 1, 0]) == 1


def test_2():
    assert dominantIndex([1, 2, 3, 4]) == -1
