from py2923 import findChampion


def test_1():
    assert findChampion([[0, 1], [0, 0]]) == 0


def test_2():
    assert findChampion([[0, 0, 1], [1, 0, 1], [0, 0, 0]]) == 1
