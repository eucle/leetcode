def repeatedSubstringPattern(s: str) -> bool:
    for i in range(len(s) // 2, 0, -1):
        if s[:i] * (len(s) // i) == s:
            return True
    return False


print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abcabcabcabc"))
