def isAcronym(words: list[str], s: str) -> bool:
    return ''.join([word[0] for word in words]) == s


print(isAcronym(words=["alice", "bob", "charlie"], s="abc"))
print(isAcronym(words=["an", "apple"], s="a"))
print(isAcronym(words=["never", "gonna", "give", "up", "on", "you"],
                s="ngguoy"))
