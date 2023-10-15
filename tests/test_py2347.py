from py2347 import bestHand


def test_1():
    ranks = [13, 2, 3, 1, 9]
    suits = ["a", "a", "a", "a", "a"]
    assert bestHand(ranks, suits) == "Flush"


def test_2():
    ranks = [4, 4, 2, 4, 4]
    suits = ["d", "a", "a", "b", "c"]
    assert bestHand(ranks, suits) == "Three of a Kind"
