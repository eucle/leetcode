def canBeEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True
    res = list(s1)
    res[0], res[2] = res[2], res[0]
    if ''.join(res) == s2:
        return True
    res[1], res[3] = res[3], res[1]
    if ''.join(res) == s2:
        return True
    res[0], res[2] = res[2], res[0]
    if ''.join(res) == s2:
        return True
    return False


print(canBeEqual("abcd", "cdab"))
print(canBeEqual("abcd", "dacb"))
