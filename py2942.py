def findWordsContaining(words: list[str], x: str) -> list[int]:
    return [i for i, v in enumerate(words) if x in set(v)]
