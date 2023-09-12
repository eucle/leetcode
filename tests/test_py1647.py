from py1647 import minDeletions


def test_1():
    assert minDeletions('aab') == 0


def test_2():
    assert minDeletions('aaabbbcc') == 2


def test_3():
    assert minDeletions('ceabaacb') == 2
