from collections import Counter


def minDeletions(s: str) -> int:
    checking, cntr = set(), 0
    for num in Counter(s).values():
        if num not in checking:
            checking.add(num)
        else:
            while num in checking and num > 0:
                num -= 1
                cntr += 1
            checking.add(num)
    return cntr
