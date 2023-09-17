from collections import Counter


def beautySum(s: str) -> int:
    cnt = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            cnt_dict = Counter(s[i:j])
            cnt_dict_values = cnt_dict.values()
            cnt += (max(cnt_dict_values) - min(cnt_dict_values))
    return cnt
