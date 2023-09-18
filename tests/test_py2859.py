from py2859 import sumIndicesWithKSetBits


def test_1():
    assert sumIndicesWithKSetBits([5, 10, 1, 5, 2], 1) == 13


def test_2():
    assert sumIndicesWithKSetBits([4, 3, 2, 1], 2) == 1
