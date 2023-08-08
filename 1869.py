def checkZeroOnes(s: str) -> bool:
    return len(max(s.split('1'))) < len(max(s.split('0')))


print(checkZeroOnes("1101"))
print(checkZeroOnes("111000"))
print(checkZeroOnes("110100010"))
