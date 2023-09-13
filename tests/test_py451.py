from py451 import frequencySort


def test_1():
    assert frequencySort("tree") == "eetr"


def test_2():
    assert frequencySort("cccaaa") == "cccaaa"
