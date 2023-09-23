from py2224 import convertTime


def test_1():
    assert convertTime("02:30", "04:35") == 3


def test_2():
    assert convertTime("11:00", "11:01") == 1
