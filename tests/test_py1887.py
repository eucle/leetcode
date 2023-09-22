from py1887 import reductionOperations


def test_1():
    assert reductionOperations([5, 1, 3]) == 3


def test_2():
    assert reductionOperations([1, 1, 2, 2, 3]) == 4
