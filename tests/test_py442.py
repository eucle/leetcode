from py442 import findDuplicates


def test_01():
    assert findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]) == [2, 3]


def test_2():
    assert findDuplicates([1, 1, 2]) == [1]
