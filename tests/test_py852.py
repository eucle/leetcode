from py852 import peakIndexInMountainArray


def test_1():
    assert peakIndexInMountainArray([0, 1, 0]) == 1


def test_2():
    assert peakIndexInMountainArray([0, 2, 1, 0]) == 1


def test_3():
    assert peakIndexInMountainArray([0, 10, 5, 2]) == 1
