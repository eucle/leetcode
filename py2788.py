def splitWordsBySeparator(words: list[str], separator: str) -> list[str]:
    res = []
    for word in words:
        word = word.replace(separator, ' ')
        res += word.split()
    return res


print(splitWordsBySeparator(["one.two.three", "four.five", "six"], "."))
print(splitWordsBySeparator(words=["$easy$", "$problem$"], separator="$"))
print(splitWordsBySeparator(words=["|||"], separator="|"))
