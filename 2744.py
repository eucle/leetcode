def maximumNumberOfStringPairs(words: list[str]) -> int:
    return int(sum([w[::-1] in words and w != w[::-1] for w in words]) / 2)


print(maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]))
print(maximumNumberOfStringPairs(["ab", "ba", "cc"]))
