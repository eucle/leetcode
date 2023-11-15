from py2309 import greatestLetter


def test_1():
    assert greatestLetter("lEeTcOdE") == "E"


def test_2():
    assert greatestLetter("arRAzFif") == "R"


def test_3():
    assert greatestLetter("AbCdEfGhIjK") == ""
