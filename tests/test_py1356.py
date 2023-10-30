from py1356 import sortByBits


def test_1():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    res = [0, 1, 2, 4, 8, 3, 5, 6, 7]
    assert sortByBits(arr) == res


def test_2():
    arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    res = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    assert sortByBits(arr) == res
