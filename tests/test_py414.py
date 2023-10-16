from py414 import thirdMax


def test_1():
    assert thirdMax([3, 2, 1]) == 1


def test_2():
    assert thirdMax([1, 2]) == 2


def test_3():
    assert thirdMax([2, 2, 3, 1]) == 1
