def finalString(s: str) -> str:
    res = ''
    for char in s:
        if char == 'i':
            res = res[::-1]
        else:
            res += char
    return res


print(finalString('string'))
print(finalString('poiinter'))
