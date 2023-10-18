from py1630 import checkArithmeticSubarrays


def test_1():
    nums = [4, 6, 5, 9, 3, 7]
    le = [0, 0, 2]
    r = [2, 3, 5]
    assert checkArithmeticSubarrays(nums, le, r) == [True, False, True]
