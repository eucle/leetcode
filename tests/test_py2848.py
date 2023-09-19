from py2848 import numberOfPoints


def test_1():
    assert numberOfPoints([[3, 6], [1, 5], [4, 7]]) == 7


def test_2():
    assert numberOfPoints([[1, 3], [5, 8]]) == 7
