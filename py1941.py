def areOccurrencesEqual(s: str) -> bool:
    dictio: dict = {}
    for ch in s:
        dictio[ch] = dictio.get(ch, 0) + 1
    return len(set(dictio.values())) == 1


print(areOccurrencesEqual("abacbc"))
print(areOccurrencesEqual("aaabb"))
