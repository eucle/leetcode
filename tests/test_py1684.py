from py1684 import countConsistentStrings


def test_1():
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    assert countConsistentStrings(allowed, words) == 2


def test_2():
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    assert countConsistentStrings(allowed, words) == 7


def test_3():
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    assert countConsistentStrings(allowed, words) == 4
