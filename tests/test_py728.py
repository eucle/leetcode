from py728 import selfDividingNumbers


def test_1():
    left = 1
    right = 22
    res = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert selfDividingNumbers(left, right) == res


def test_2():
    left = 47
    right = 85
    res = [48, 55, 66, 77]
    assert selfDividingNumbers(left, right) == res
