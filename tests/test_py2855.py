from py2855 import minimumRightShifts


def test_1():
    assert minimumRightShifts([3, 4, 5, 1, 2]) == 2


def test_2():
    assert minimumRightShifts([1, 3, 5]) == 0


def test_3():
    assert minimumRightShifts([2, 1, 4]) == -1
