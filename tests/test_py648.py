from py648 import replaceWords


def test_1():
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    res = "the cat was rat by the bat"
    assert replaceWords(dictionary, sentence) == res


def test_2():
    dictionary = ["a", "b", "c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    res = "a a b c"
    assert replaceWords(dictionary, sentence) == res
