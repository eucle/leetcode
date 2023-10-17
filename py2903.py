def findIndices(nums: list[int], indexDifference: int,
                valueDifference: int) -> list[int]:
    for ii, iv in enumerate(nums):
        for ji, jv in enumerate(nums):
            if (abs(ii - ji) >= indexDifference and
                    abs(iv - jv) >= valueDifference):
                return [ii, ji]
    return [-1, -1]
