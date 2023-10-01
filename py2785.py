def sortVowels(s: str) -> str:
    all_vows, res, idx = {65, 69, 73, 79, 85, 97, 101, 105, 111, 117}, [], 0
    vows = [sym for sym in s if ord(sym) in all_vows]
    vows.sort()
    for sym in s:
        if ord(sym) in all_vows:
            res.append(vows[idx])
            idx += 1
        else:
            res.append(sym)
    return ''.join(res)


print(sortVowels("lEetcOde"))
print(sortVowels("lYmpH"))
