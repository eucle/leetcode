from py2363 import mergeSimilarItems


def test_1():
    items1 = [[1, 1], [4, 5], [3, 8]]
    items2 = [[3, 1], [1, 5]]
    assert mergeSimilarItems(items1, items2) == [[1, 6], [3, 9], [4, 5]]


def test_2():
    items1 = [[1, 1], [3, 2], [2, 3]]
    items2 = [[2, 1], [3, 2], [1, 3]]
    assert mergeSimilarItems(items1, items2) == [[1, 4], [2, 4], [3, 4]]


def test_3():
    items1 = [[1, 3], [2, 2]]
    items2 = [[7, 1], [2, 2], [1, 4]]
    assert mergeSimilarItems(items1, items2) == [[1, 7], [2, 4], [7, 1]]
