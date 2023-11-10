from py961 import repeatedNTimes


def test_1():
    assert repeatedNTimes([1, 2, 3, 3]) == 3


def test_2():
    assert repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2
