from py1534 import countGoodTriplets


def test_1():
    arr = [3, 0, 1, 1, 9, 7]
    a = 7
    b = 2
    c = 3
    assert countGoodTriplets(arr, a, b, c) == 4


def test_2():
    arr = [1, 1, 2, 2, 3]
    a = 0
    b = 0
    c = 1
    assert countGoodTriplets(arr, a, b, c) == 0
