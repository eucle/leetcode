def minimizedStringLength(s: str) -> int:
    return len(set(s))


print(minimizedStringLength('aaabc'))
print(minimizedStringLength('cbbd'))
print(minimizedStringLength('dddaaa'))
