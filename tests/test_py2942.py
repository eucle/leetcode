from py2942 import findWordsContaining


def test_1():
    words = ["leet", "code"]
    x = "e"
    assert findWordsContaining(words, x) == [0, 1]


def test_2():
    words = ["abc", "bcd", "aaaa", "cbc"]
    x = "a"
    assert findWordsContaining(words, x) == [0, 2]


def test_3():
    words = ["abc", "bcd", "aaaa", "cbc"]
    x = "z"
    assert findWordsContaining(words, x) == []
