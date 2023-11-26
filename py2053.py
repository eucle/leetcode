from collections import Counter


def kthDistinct(arr: list[str], k: int) -> str:
    cntr = Counter(arr)
    for string in arr:
        if cntr[string] == 1:
            if k > 1:
                k -= 1
            else:
                return string
    return ""
