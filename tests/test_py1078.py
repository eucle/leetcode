from py1078 import findOcurrences


def test_1():
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    res = ["girl", "student"]
    assert findOcurrences(text, first, second) == res


def test_2():
    text = "we will we will rock you"
    first = "we"
    second = "will"
    res = ["we", "rock"]
    assert findOcurrences(text, first, second) == res
