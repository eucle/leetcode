from py349 import intersection


def test_1():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert intersection(nums1, nums2) == [2]


def test_2():
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert intersection(nums1, nums2) == [4, 9]
