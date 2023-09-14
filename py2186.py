from collections import Counter


def minSteps(s: str, t: str) -> int:
    s_counter: Counter = Counter(s)
    s_counter.subtract(Counter(t))
    return sum(map(abs, s_counter.values()))
