import pytest

from py2053 import kthDistinct


@pytest.mark.parametrize("arr, k, ans", [
    (["d", "b", "c", "b", "c", "a"], 2, "a"),
    (["aaa", "aa", "a"], 1, "aaa"),
    (["a", "b", "a"], 3, "")
],
    ids=["first_example", "second_example", "third_example"]
)
def test_kthDistinct(arr, k, ans):
    """Тест для проверки трех примеров"""
    assert kthDistinct(arr, k) == ans
