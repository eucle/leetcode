def canBeTypedWords(text: str, brokenLetters: str) -> int:
    return sum([set(w).isdisjoint(brokenLetters) for w in text.split()])


print(canBeTypedWords("hello world", "ad"))
print(canBeTypedWords("leet code", "lt"))
print(canBeTypedWords("leet code", "e"))
