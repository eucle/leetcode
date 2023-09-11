from py1637 import maxWidthOfVerticalArea


def test_1():
    points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    assert maxWidthOfVerticalArea(points) == 3


def test_2():
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    assert maxWidthOfVerticalArea(points) == 1
