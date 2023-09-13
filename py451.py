from collections import Counter


def frequencySort(s: str) -> str:
    res = Counter(s)
    return ''.join([v * k for k, v in sorted(res.items(),
                                             key=lambda x: x[1],
                                             reverse=True)])
