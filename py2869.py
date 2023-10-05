from typing import List


def minOperations(nums: List[int], k: int) -> int:
    collection = {i for i in range(1, k + 1)}
    cnt = 0
    while collection:
        rem = nums.pop()
        if rem in collection:
            collection.remove(rem)
        cnt += 1
    return cnt
