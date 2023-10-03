def isFascinating(n: int) -> bool:
    string = list(str(n) + str(n * 2) + str(n * 3))
    return len(string) == len(set(string)) == 9 and '0' not in string


print(isFascinating(192))
print(isFascinating(100))
