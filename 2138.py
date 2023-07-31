def divideString(s: str, k: int, fill: str) -> list[str]:
    return [s[i:i+k] + fill * (k-len(s[i:i+k])) for i in range(0, len(s), k)]


print(divideString(s="abcdefghi", k=3, fill="x"))
print(divideString(s="abcdefghij", k=3, fill="x"))
