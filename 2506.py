def similarPairs(words: list[str]) -> int:
    return sum(set(words[i]) == set(words[j]) for i in range(len(words))
               for j in range(i, len(words)) if i != j)


print(similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))
